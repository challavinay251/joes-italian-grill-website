from django.urls import path
from .views import home
from .views import home, menu, gallery, faq

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('gallery/', gallery, name='gallery'),
    path('faq/', faq, name='faq'),
]