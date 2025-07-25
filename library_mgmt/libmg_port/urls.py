from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('shop', shopping_cart, name='shopping'),  # Change 'shopping' to 'shop'
    path('save',save_student),
]