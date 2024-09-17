from django.urls import path
from . import views


urlpatterns = [
    path('', views.sites, name='sites'),
    path('delete_image_general/<int:building_id>/', views.delete_image_general, name='delete_image_general'),
    path('delete_image_contacts/<int:contact_id>/', views.delete_image_contacts, name='delete_image_contacts'),
    path('add/', views.add, name='add_s'),
    path('edit/<int:pk>/', views.edit, name='edit_s'),
    path('landing/<int:page_id>/', views.landing, name='landing'),
    path('delete/<int:pk>/', views.delete_site, name='delete_s'),
    path('buildings/', views.building_list, name='building_list'),
    path('landing_page_building/<int:page_id>/', views.landing_page_building, name='landing_page_building'),
]