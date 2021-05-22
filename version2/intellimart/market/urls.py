from django.urls import path, include
from .views import *

urlpatterns = [
    path('market', StoreView.as_view()),
    path('products', ProductView.as_view()),
    path('users', AllCustomerView.as_view()),
    path('cart', CartView.as_view()),
    path('cartprod', CartProductView.as_view()), 
    path('slots', SlotView.as_view()), 
    path('register', RegisterCustomer.as_view()),
    path('login', LoginCustomer.as_view())
]
