from django.urls import path
from . import views


urlpatterns = [
    path('', views.sites, name='sites'),
    path('add/', views.add, name='add_s'),
    path('edit/<int:pk>/', views.edit, name='edit_s'),
    path('landing/<int:page_id>/', views.landing, name='landing'),
]