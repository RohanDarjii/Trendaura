from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login , logout , authenticate
from accounts.models import Cart,Cart_items
from products.models import Coupon, Products, ProductImage
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')

@never_cache
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(first_name = first_name, last_name = last_name, email= email, username = email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'Account created.')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/register.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def cart(request):
    cart = Cart.objects.get(is_paid= False, user = request.user)
    if request.method == 'POST':
        coupon_code = request.POST.get('coupon_code')
        coupon_qs = Coupon.objects.filter(coupon_code__iexact = coupon_code)
        if not coupon_qs.exists():
            messages.warning(request,"Invalid coupon code")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        coupon = coupon_qs.first()
        if cart.coupon:
            messages.warning(request, "This coupon is already applied.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if cart.get_cart_total() < coupon.min_amount:
            messages.info(request, f"Minimum amount should be greater than {coupon.min_amount}")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if coupon.is_expired:
            messages.warning(request, "This code is expired")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        cart.coupon = coupon
        cart.save()
        messages.success(request,f"Coupon '{coupon_code}' applied successfully!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {'cart': cart }
    return render(request, 'accounts/cart.html', context)

def remove_cart_item(request,item_uid):
    item = Cart_items.objects.get(uid=item_uid)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_coupon(request, cart_uid):
    cart = Cart.objects.get(uid = cart_uid)
    cart.coupon = None
    cart.save()
    messages.success(request,"Coupon removed")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def update_quantity(request, item_id):
    item = get_object_or_404(Cart_items, id=item_id, cart__user=request.user, cart__is_paid=False)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        item.quantity = quantity
        item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))