from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('modify/<item_id>/', views.modify_bag, name='modify_bag'),
    path('remove/<item_id>/', views.remove_bag_item, name='remove_bag_item'),


]
