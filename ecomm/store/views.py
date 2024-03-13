from django.shortcuts import render
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
            print(size)
            
        
        return render(request, 'store/product.html', context)
    except Exception as e:
        print(e)
        
        
def add_to_cart(request, slug):
    varient = request.GET.get('varient')
    product = Product.objects.get(slig = slug )
    user = request.user
    cart , create = Cart.objects.get_or_create(user = user, is_paid=False)
    
    return HttpResponseRedirect(request.path_info)