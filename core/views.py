from django.db.models import Q
from django.shortcuts import render
from products.models import Category, Product

def home(request):
    best_sellers = Product.objects.filter(is_best_seller=True)[:3]
    products = Product.objects.all()[:6]

    return render(request, 'home.html', {
        'best_sellers': best_sellers,
        'products': products
    })

def menu(request):
    query = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category')

    categories = Category.objects.all()
    products = Product.objects.all()

    # SMART SEARCH
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )

    # CATEGORY FILTER
    if selected_category:
        products = products.filter(category_id=selected_category)

    # GROUP BY CATEGORY (CLEAN UI)
    category_products = []
    for category in categories:
        cat_products = products.filter(category=category)
        if cat_products.exists():
            category_products.append({
                'category': category,
                'products': cat_products
            })

    return render(request, 'menu.html', {
        'categories': categories,
        'category_products': category_products,
        'query': query,
        'selected_category': selected_category,
        'result_count': products.count()
    })