from django.urls import path
from checkout import views


urlpatterns = [
    path('strip', views.strip_transaction, name='checkout.strip'),
    path('paypal', views.paypal_transaction, name='checkout.paypal'),
]