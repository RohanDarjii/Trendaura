from django.urls import path
from accounts.views import login_page, logout_page, register_page, cart, remove_cart_item, remove_coupon, update_quantity
from products.views import add_to_cart
urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout_page'),
    path('cart/',cart, name='cart'),
    path('add_to_cart/<uid>/', add_to_cart, name='add_to_cart'), 
    path('remove_cart_item/<item_uid>/', remove_cart_item , name='remove_cart_item'),
    path('remove-coupon/<cart_uid>/', remove_coupon, name='remove_coupon'), 
]
