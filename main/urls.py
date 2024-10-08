from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('objects/add/', views.add, name='add'),
    path('objects/edit/<int:pk>', views.edit, name='edit'),  # Маршрут для добавления нового объекта
    path('objects/delete/<int:pk>/', views.delete, name='delete'),
    path('objects/delete_image/<int:pk>/<str:image_type>/', views.delete_image, name='delete_image'),
    path('objects/delete_image_building/<int:building_id>/', views.delete_image_building, name='delete_image_building'),
    path('objects/delete_plans/<int:pk>/', views.delete_plans, name='delete_plans'),
]
