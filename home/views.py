from django.shortcuts import render
from products.models import Products
from accounts.models import Cart
# Create your views here.
def index(request):
    context = {'products': Products.objects.all()}
    return render(request, 'home/index.html', context)  