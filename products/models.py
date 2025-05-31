from datetime import timezone
from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

# Create your models here.
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to='catgories')

    def save(self,*args, **kwargs):
        self.slug = slugify(self.category_name)
        return super(Category, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.category_name
    
class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.color_name
    
class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.size_name
    
class Products(BaseModel):
    products_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    products_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    products_descriptions = models.TextField()
    products_price = models.IntegerField()
    products_size = models.ManyToManyField(SizeVariant, blank=True)
    products_color = models.ManyToManyField(ColorVariant, blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.products_name)
        return super(Products, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.products_name
    
    def get_product_price_by_size(self, size):
        return self.products_price + SizeVariant.objects.get(size_name = size).price



class ProductImage(BaseModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product')

class Coupon(BaseModel):
    coupon_code = models.CharField(max_length=20, unique=True)
    discount_price = models.IntegerField()
    is_expired = models.BooleanField(default=False)
    min_amount = models.IntegerField(default=0)