from django.shortcuts import render, redirect
from .models import *
from accounts.models import *

from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)



def get_products(request, slug):
    try:
        product = Product.objects.get(slug = slug)
        
        context = {
            'product':product
        }
        
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_bySize(size)
            context['selected_size'] = size
            context['updated_price'] = price            
        
        return render(request, 'store/product.html', context)
    except Exception as e:
        print(e)
        
        
def add_to_cart(request, uid):
    varient = request.GET.get('varient')
    
    product = Product.objects.get(uid= uid )
    user = request.user
    cart , create = Cart.objects.get_or_create(user = user, is_paid=False)
    
    cart_item = CartItems.objects.create(cart = cart, product = product)
    
    if varient:
        varient = request.GET.get('varient')
        size_varient = SizeVarient.objects.get(size = varient)
        cart_item.size_varient = size_varient
        cart_item.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))