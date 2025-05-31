
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from products.models import Products, SizeVariant, ColorVariant
from accounts.models import Cart, Cart_items


def get_product(request , slug):
    try:
        product = Products.objects.get(slug =slug)
        context = {'product' : product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price

        return render(request  , 'product/product.html', context = context)
    except Exception as e:
        print(e)

def add_to_cart(request, uid):
    variant = request.GET.get('variant')
    product = Products.objects.get(uid = uid)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

    size = None
    if variant:
        size = get_object_or_404(SizeVariant, size_name=variant)

    cart_item = Cart_items.objects.create(
        cart=cart,
        product=product,
        products_size=size
    )



    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

