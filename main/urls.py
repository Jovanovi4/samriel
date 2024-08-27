from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('objects/add/', views.add, name='add'),
    path('objects/edit/<int:pk>/', views.edit, name='edit'),  # Маршрут для добавления нового объекта
    path('objects/delete/<int:pk>/', views.delete, name='delete'),
]
