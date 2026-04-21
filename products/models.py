from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg'),
    ]

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=[
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg')
    ])
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    is_best_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.name