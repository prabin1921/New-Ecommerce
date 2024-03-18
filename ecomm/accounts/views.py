from django.shortcuts import render, redirect, HttpResponse, get_list_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from .models import *



def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = email)

        if not user.exists():
            messages.warning(request , "Account not found")
            return redirect('login')
        
        if not user[0].profile.is_verified:
            messages.warning(request, "Your email is not verified! Verify First")
            return redirect('login')
        
        user = authenticate(username = email, password=password)
        if user:
            login(request , user)
            return redirect("/")
       
        messages.warning(request, "Invalid Credentials")
        
        return redirect('register')
    
    return render(request, 'accounts/login.html')



def register_page(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = email)

        if user.exists():
            messages.warning(request, "Email is already registered! Log in below.")
            return redirect('register')
        
        user=User.objects.create(first_name=first_name, last_name=last_name, email=email, username = email)
        user.set_password(password)
        user.save()
       
        messages.success(request, "Code Has been send to your mail!")
        return redirect('register')
         
    return render(request, 'accounts/register.html')


def activate_email(request, email_token):
    try:
        user= Profile.objects.get(email_token = email_token)
        user.is_verified=True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email Token')
    
def get_cart_count(request):
    if request.user.is_authenticated:
        cart_count = CartItems.objects.filter(cart__is_paid=False, cart__user=request.user).count()
        return JsonResponse({'cart_count': cart_count})
    else:
        return JsonResponse({'cart_count': 0})
    
def get_cart_total(request):
    cart_items = request.cart_items.all()
    
    
def cart(request):
    user = request.user
    user_cart = Cart.objects.filter(user = request.user.pk, is_paid = False).first()
    if user_cart:
        cart_items = CartItems.objects.filter(cart=user_cart.uid)
        print(cart_items)
        item_total = [item.product.price * item.quantity  for item in cart_items if item.product.price and item.quantity]
        total_price = sum(item_total)
        print(total_price)
        discount = 60.00  # Assume there is a $60 discount
        tax = 13.00  # Assume there is a $14 tax
        total_price_after_discount_and_tax = total_price - (discount + tax)
            
        
    else:
        cart_items = []
        total_price = 0
        discount = 0
        tax = 0
        total_price_after_discount_and_tax = 0
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'discount': discount,
        'tax': tax,
        'total_price_after_discount_and_tax': (total_price_after_discount_and_tax),
    }
    return render(request, 'accounts/cart.html', context)
