from django.urls import path
from checkout import views


urlpatterns = [
    path('order', views.makeOrder, name='checkout.order')
]