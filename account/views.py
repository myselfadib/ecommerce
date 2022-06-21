from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from requests import request

#from orders.views import user_orders

from .forms import RegistrationForm
from .models import UserBase
from .tokens import account_activation_token


@login_required
# Create your views here.

def account_register(request):
   # if request.user.is_authenticated:
    #    return redirect('/')
    if request.method == 'POST':
        registerForm =  RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password = registerForm.cleaned_data['password']
            user.is_active = False
            user.save()

            # setup email
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('account/registration/account_activation_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject,message=message)
    else:
        registerForm = RegistrationForm()
    return render(request,'account/registration/register.html', {'form':registerForm})
            


def account_activate(self, uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()    
        login(request,user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')    
    

def dashboard(self):
    return
    