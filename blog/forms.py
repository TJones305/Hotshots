from django import forms
from .models import NewBlog


class BlogForm(forms.ModelForm):

    class Meta:
        model = NewBlog

        exclude = ('blog_date',)

        fields = ('blog_date',
                  'blog_title',
                  'blog_description',
                  'blog_verdict',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
                'blog_date': 'Date',
                'blog_title': 'Blog Title',
                'blog_description': 'Blog Description',
                'blog_verdict': 'Blog Verdict',
        }

        self.fields['blog_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 ')
            self.fields[field].label = False
