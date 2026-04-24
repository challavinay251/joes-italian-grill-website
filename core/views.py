from django.shortcuts import render
from products.models import Category, Product


# 🏠 HOME PAGE
def home(request):
    best_sellers = Product.objects.filter(is_best_seller=True)[:3]
    products = Product.objects.all()[:6]  # for menu preview

    return render(request, 'home.html', {
        'best_sellers': best_sellers,
        'products': products
    })


# 🍽 MENU PAGE (DYNAMIC)
def menu(request):
    categories = Category.objects.prefetch_related('products').all()

    return render(request, 'menu.html', {
        'categories': categories
    })