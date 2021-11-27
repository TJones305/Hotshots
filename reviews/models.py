from django.db import models
from profiles.models import UserProfile
from products.models import Product


class UserReview(models.Model):
    """
    Model for registered users to review their products
    """
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='writer')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='item')
    date = models.DateTimeField(auto_now=True)
    review_title = models.CharField(max_length=254)
    review_description = models.TextField(blank=True, null=True, default='')
    review_rating = models.DecimalField(max_digits=1, decimal_places=0,
                                        null=True, blank=True)

    def __str__(self):
        return self.review_title
