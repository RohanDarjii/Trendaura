from django.contrib import admin
from .models import Profile, Cart,Cart_items
# Register your models here.

admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Cart_items)