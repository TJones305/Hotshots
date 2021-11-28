from django.contrib import admin
from .models import NewBlog


class NewBlogAdmin(admin.ModelAdmin):
    fields = ('date',
              'blog_title',
              'blog_description',
              'blog_verdict',
              )

    list_display = ('blog_title',
                    'blog_description',
                    'blog_verdict',
                    )

    ordering = ('blog_title',)


admin.site.register(NewBlog, NewBlogAdmin)
