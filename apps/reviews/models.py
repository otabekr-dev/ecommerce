from django.db import models
from apps.products.models import Product
from apps.accounts.models import User

# Review: product, user, rate, comment

class Review(models.Model):
    RatingChoices = [
        [1, '1'],
        [2, '2'],
        [3, '3'],
        [4, '4'],
        [5, '5'],
    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='product_reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='user_reviews'
    )
    rate = models.IntegerField(choices=RatingChoices, null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return f'{self.rate} | {self.comment}'
    
    def to_dict(self):
        return {
            "id": self.pk,
            "product": self.product.id,
            "user" : self.user.pk,
            "rate" : self.rate,
            "comment": self.comment 
        }