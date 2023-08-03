from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    in_favorite = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Product name: {self.name} | quantity: {self.quantity}'

    def increase_product_rate(self):
        self.in_favorite += 1

    def decrease_product_rate(self):
        if int(self.in_favorite) > 0:
            self.in_favorite -= 1
