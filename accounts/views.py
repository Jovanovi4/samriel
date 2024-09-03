from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import logout as auth_logout
from django.urls import reverse
from django.http import JsonResponse
from .forms import CustomAuthenticationForm
from .models import CustomUser
from django.contrib import messages




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Перенаправление на домашнюю страницу после регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Перенаправление на домашнюю страницу после входа
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':    
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')  # Перенаправление на страницу профиля после сохранения
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect(reverse('accounts:login'))


@login_required
def delete_image_user(request, user_id):
    if request.method == 'POST':
        try:
            user = get_object_or_404(CustomUser, pk=user_id)
            if user.image:
                user.image.delete(save=False)  # Удаляет файл изображения с диска
                user.image = None  # Очищает поле image в модели
                user.save()  # Сохраняет изменения в базе данных
            return redirect('accounts:profile')  # Перенаправление на профиль пользователя после удаления изображения
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)
    return redirect('accounts:profile')