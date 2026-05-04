from django.urls import path
from .views import home, menu, gallery,offers , contact

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('gallery/', gallery, name='gallery'),
    path('offers/', offers, name='offers'),
    path('contact/', contact, name='contact'),
]