import json

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from basket.basket import Basket
#from orders.views import payment_confirmation

# Create your views here.
@login_required  
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51LGNYHK9Mq6UmztsyW63k9TTi4nbfBzoew7qsMxkgFRcfaiKvSs5NMsr6K6U8PKwx4BtH5TI39uxcY3C24J9HQDL004yG4wz95'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
    return render(request, 'payment/home.html', {'client_secret':intent.client_secret})

