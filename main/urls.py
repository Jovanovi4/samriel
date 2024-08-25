from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),  # Маршрут для добавления нового объекта
    path('edit/<int:pk>/', views.edit, name='edit_with_pk'),  # Маршрут для редактирования существующего объекта
    path('delete/<int:pk>/', views.delete, name='delete'),
]
