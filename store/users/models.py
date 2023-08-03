from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import Product


class User(AbstractUser):
    def __str__(self):
        return f'User: {self.username}'


class Favorite(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='favorite')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='favorite')

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['user', 'product'],
            name='unique_product_for_user'
        )]

    def __str__(self):
        return f'Favorite: {self.product.name}'
