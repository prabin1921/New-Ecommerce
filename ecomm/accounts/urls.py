from django.urls import path


from .import views
from .views import *
from store.views import add_to_cart


urlpatterns = [
    path('login/', views.login_page, name = "login"),
    path('register/', views.register_page, name = "register"),
    path('activate/<email_token>/', views.activate_email, name = "activate_email"),
    path('get_cart_count/', views.get_cart_count, name='get_cart_count'),
    path('cart/', views.Cart, name='cart')
    
    ]