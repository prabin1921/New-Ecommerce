from django.urls import path


from .import views
from .views import *


urlpatterns = [
    path('login/', views.login_page, name = "login"),
    path('register/', views.register_page, name = "register"),
    path('activate/<email_token>/', views.activate_email, name = "activate_email"),
    ]