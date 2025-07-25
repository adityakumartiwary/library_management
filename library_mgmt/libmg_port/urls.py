from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),  # This maps the root URL to the home view
    path('home/', home, name='home'),
    path('shop', shopping_cart, name='shopping'),
    path('save', save_student),
]