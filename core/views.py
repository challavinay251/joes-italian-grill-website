from django.db.models import Q
from products.models import Category, Product
from .models import Gallery
from products.models import Product
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from core.models import Testimonial

def home(request):
    best_sellers = Product.objects.filter(is_best_seller=True)
    products = Product.objects.all()[:6]
    testimonials = Testimonial.objects.all().order_by('-rating', '-created_at')[:6]

    return render(request, 'home.html', {
        'best_sellers': best_sellers,
        'products': products,
        'testimonials': testimonials,
    })

def faq(request):
    return render(request, 'faq.html')

def offers(request):
    offers = Product.objects.filter(is_offer=True)

    return render(request, 'offers.html', {
        'offers': offers
    })

def menu(request):
    query = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category')

    categories = Category.objects.all()
    products = Product.objects.all()

    # BEST SELLERS (FOR POPULAR SECTION)
    best_sellers = Product.objects.filter(is_best_seller=True)[:6]

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
        'best_sellers': best_sellers,
        'query': query,
        'selected_category': selected_category,
        'result_count': products.count()
    })



def gallery(request):
    images = Gallery.objects.all().order_by('-id')
    return render(request, 'gallery.html', {'images': images})


def contact(request):
    success = False

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"""
New Contact Message

Name: {name}
Email: {email}

Message:
{message}
"""

        send_mail(
            subject=f"New Contact Message from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],  # send to yourself
        )

        success = True

    return render(request, 'contact.html', {'success': success})