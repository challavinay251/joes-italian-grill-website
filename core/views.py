from django.shortcuts import render
from products.models import Product   # make sure this import is there

def home(request):
    products = Product.objects.all()
    best_sellers = Product.objects.all()[:3]

    return render(request, 'home.html', {
        'products': products,
        'best_sellers': best_sellers
    })