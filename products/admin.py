from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'image_preview',
        'name',
        'category',
        'price',
        'discount',
        'final_price',
        'is_offer',
        'is_best_seller'
    )

    list_filter = (
        'category',
        'is_offer',
        'is_best_seller'
    )

    search_fields = ('name', 'description')

    list_editable = (
        'discount',
        'is_offer',
        'is_best_seller'
    )

    readonly_fields = ('image_preview_large', 'final_price')

    fieldsets = (
        ('📦 Basic Info', {
            'fields': ('name', 'category', 'price', 'description', 'image', 'image_preview_large')
        }),

        ('⭐ Flags', {
            'fields': ('is_best_seller', 'is_offer')
        }),

        ('🔥 Offer Details', {
            'fields': ('discount', 'offer_label', 'final_price'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="border-radius:5px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Image"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" style="border-radius:10px;" />', obj.image.url)
        return "-"
    image_preview_large.short_description = "Preview"

    def final_price(self, obj):
        return f"${obj.get_discounted_price():.2f}"
    final_price.short_description = "Final Price"