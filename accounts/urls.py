from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings




app_name= 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('delete_image_user/<int:user_id>/', views.delete_image_user, name='delete_image_user'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)