from django.urls import path
from . import views


urlpatterns = [
    path('', views.sites, name='sites'),
    path('add/', views.add, name='add_s'),
    path('edit/<int:pk>/', views.edit, name='edit_s'),
    path('landing/<int:page_id>/', views.landing, name='landing'),
    path('delete_image_contacts/<int:contacts_id>/', views.delete_image_contacts, name='delete_image_contacts'),
    path('delete_image_general/<int:building_id>/', views.delete_image_general, name='delete_image_general'),
]