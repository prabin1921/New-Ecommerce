from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name = "home"),
    path('<slug>/', views.get_products, name = "product"),
    path('add-to-cart/<uid>/', views.add_to_cart, name = "add_to_cart"),
]
