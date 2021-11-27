from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_reviews, name='product_reviews'),
    path('add/', views.add_review, name='add_review'),
    path('edit/', views.edit_review, name='edit_review'),
]
