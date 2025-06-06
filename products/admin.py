from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model =ProductImage

class ProductsAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]   


@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name' , 'price']
    model = ColorVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name' , 'price']

    model = SizeVariant

admin.site.register(Products, ProductsAdmin)

admin.site.register(ProductImage)

admin.site.register(Coupon)