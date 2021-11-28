from django.db import models


class NewBlog(models.Model):
    """
    Model for registered users to review their products
    """
    class Meta:
        verbose_name_plural = "Blogs"

    blog_title = models.CharField(max_length=254)
    blog_date = models.DateTimeField(auto_now=True)
    blog_description = models.TextField(blank=False, null=True, default='')
    blog_verdict = models.CharField(max_length=254, blank=False, null=True,
                                    default='')

    def __str__(self):
        return self.blog_title
