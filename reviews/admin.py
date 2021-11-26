from django.contrib import admin
from .models import UserReview


class UserReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('user',
                       'date',
                       'review_rating',
                       )

    fields = ('user', 'date',
              'review_title',
              'review_description',
              'review_rating',
              'product'
              )

    list_display = (
        'user',
        'date',
        'review_title',
        'review_description',
        'review_rating',
    )

    ordering = ('date',)

admin.site.register(UserReview, UserReviewAdmin)
