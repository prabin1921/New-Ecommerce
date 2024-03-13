from django.urls import path


from .import views
from .views import *
from store.views import add_to_cart


urlpatterns = [
    path('login/', views.login_page, name = "login"),
    path('register/', views.register_page, name = "register"),
    path('activate/<email_token>/', views.activate_email, name = "activate_email"),
    # path('cart/', views.cart, name='cart'),
    path('add-to-cart/', add_to_cart, name = "add_to_cart"),
    ]