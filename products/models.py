# from django.db import models
#
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
#
#     price = models.FloatField()
#     description = models.TextField(blank=True)
#
#     image = models.ImageField(upload_to='products/', blank=True, null=True)
#
#     is_best_seller = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    # ORIGINAL PRICE
    price = models.FloatField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    # FLAGS
    is_best_seller = models.BooleanField(default=False)
    is_offer = models.BooleanField(default=False)
    # OFFER DATA
    discount = models.IntegerField(null=True, blank=True)  # e.g. 20 means 20%
    offer_label = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def get_discounted_price(self):
        if self.discount:
            return self.price - (self.price * self.discount / 100)
        return self.price
    def get_savings(self):
        if self.discount:
            return (self.price * self.discount / 100)
        return 0

    def __str__(self):
        return self.name