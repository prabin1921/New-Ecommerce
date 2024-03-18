from django.db import models
from django.contrib.auth.models import User

from base.models import *
from base.email import *
from store.models import *

from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    is_verified = models.BooleanField(default = False)
    email_token = models.CharField(max_length = 100, null =True, blank = True)
    user_image= models.ImageField(upload_to='profile')
    
    def __str__(self):
        return self.user.username
    
    
class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'carts')
    is_paid = models.BooleanField(default = False)
    
    
    def __str__(self):
        return str(self.user)

    
class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = 'cart_itmes')
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True, blank = True)
    size_varient = models.ForeignKey(SizeVarient, on_delete=models.SET_NULL, null =True, blank = True)
    color_varient = models.ForeignKey(ColorVarient, on_delete= models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null = True, blank = True)
    
    
    def __str__(self):
        return str(self.product)
    

    
@receiver(post_save, sender = User)
def send_email_token(sender, instance, created,  **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance, email_token = email_token)
            email = instance.email
            send_account_activation_email(email, email_token)
    
    except Exception as e:
        print(e)