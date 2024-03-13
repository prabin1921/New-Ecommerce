from django.db import models
from base.models import *
from django.utils.text import slugify


class Category(BaseModel):
    category_name = models.CharField(max_length = 30)
    slug = models.SlugField(unique = True, null=True, blank=True)
    category_img= models.ImageField(upload_to='catogories')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.category_name
    
    
class Product(BaseModel):
    product_name= models.CharField(max_length = 50, null=True, blank = True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'products')
    price = models.IntegerField()
    product_description = models.TextField(null= True, blank= True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.product_name
    

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'images')
    image = models.ImageField(upload_to='products')
    
    def __str__(self) -> str:
        return str(self.image)