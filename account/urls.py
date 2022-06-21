from . import views
from django.urls import path


app_name = 'account'

urlpatterns = [
    path('register/',views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>)/',views.account_activate, name='account_activate'),

    # user dashboard
    path('dashboard/',views.dashboard, name='dashboard'),


]
