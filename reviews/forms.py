from .models import UserReview
from django import forms

class ReviewForm(forms.ModelForm):

    class Meta:
        model = UserReview

        exclude = ('user', 'date',)

        fields = ('user',
                  'date',
                  'product',
                  'review_title',
                  'review_description',
                  'review_rating',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'user': 'user',
            'date': 'date',
            'product': 'product',
            'review_title': 'Review Title',
            'review_description': 'Product review here ...',
            'review_rating': ''
        }

        self.fields['review_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 ')
            self.fields[field].label = False
