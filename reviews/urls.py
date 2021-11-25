from django.urls import path
from . import views

path('<slug:slug>/', views.post_detail, name='post_detail')
