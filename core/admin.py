from django.contrib import admin
from .models import Gallery

admin.site.register(Gallery)

from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')