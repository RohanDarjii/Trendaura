from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Coupon, Products, SizeVariant,ColorVariant
class Profile(BaseModel):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    profile_image = models.ImageField(upload_to = 'profile')

    def get_cart_count(self):
        return Cart_items.objects.filter(cart__user= self.user, cart__is_paid=False).count()

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='carts' )
    is_paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)

    def get_cart_total(self):
        cart_items =self.cart_items.all()
        
        total = 0
        for item in cart_items:
            item_total = item.product.products_price
            if item.products_size:
                item_total += item.products_size.price
            if item.products_color:
                item_total += item.products_color.price
            total += item_total * item.quantity  # ✅ Multiply by quantity
        if self.coupon:
            total -= self.coupon.discount_price
        return total

class Cart_items(BaseModel):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    products_size = models.ForeignKey(SizeVariant, on_delete=models.SET_NULL, null=True,blank=True)
    products_color = models.ForeignKey(ColorVariant, on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1) 

    def get_correct_price_by_size(self):
        price = [self.product.products_price]

        if self.products_size:
            price_by_size = self.products_size.price
            price.append(price_by_size)
        if self.products_color:
            price_by_color = self.products_color.price
            price.append(price_by_color)
        return sum(price) * self.quantity
