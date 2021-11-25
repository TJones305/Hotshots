from django.contrib import admin


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('user',
                       'date',
                       'review_rating',
                       )

    fields = ('user', 'date',
              'review_title',
              'review_description',
              'review_rating',
              )

    list_display = (
        'user',
        'date',
        'review_title',
        'review_description',
        'review_rating',
    )

    ordering = ('date',)
