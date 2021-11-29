from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from profiles.models import UserProfile
from products.models import Product


class UserReview(models.Model):
    """
    Model for registered users to review their products
    """
    class Meta:
        verbose_name_plural = "Reviews"

    NO_RATING = 0
    STAY_AWAY = 1
    SUBPAR = 2
    OK = 3
    GREAT = 4
    EXCELLENT = 5

    RATING_CHOICES = [
        (NO_RATING, 'No Rating -- 0'),
        (STAY_AWAY, 'Stay Away -- 1'),
        (SUBPAR, 'Subpar -- 2'),
        (OK, 'OK -- 3'),
        (GREAT, 'Great -- 4'),
        (EXCELLENT, 'Excellent -- 5'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, blank=True,)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                null=True, blank=True,)
    date = models.DateTimeField(auto_now=True)
    review_title = models.CharField(max_length=254)
    review_description = models.TextField(blank=True, null=True, default='')
    review_rating = models.IntegerField(null=True, blank=True,
                                        choices=RATING_CHOICES,
                                        default=NO_RATING,
                                        validators=[MinValueValidator(0),
                                                    MaxValueValidator(5)])

    def __str__(self):
        return self.review_title
