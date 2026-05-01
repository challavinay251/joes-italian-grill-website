from django.urls import path
from .views import home, menu, gallery, faq ,offers , contact

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('gallery/', gallery, name='gallery'),
    path('offers/', offers, name='offers'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
]