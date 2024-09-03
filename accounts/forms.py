from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Имя",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше имя'
        }),
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        }),
    )

    class Meta:
        model = CustomUser
        fields = ('phone_number',)

        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            })
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Этот номер телефона уже зарегистрирован.")
        return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Телефон",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите номер телефона'
        }),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        }),
    )

    def confirm_login_allowed(self, user):
        # Проверка разрешений входа для пользователя
        if not user.is_active:
            raise forms.ValidationError(
                'Этот аккаунт не активен.',
                code='inactive',
            )

    def clean(self):
        # Переопределение метода clean для проверки аутентификации
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Аутентификация пользователя по номеру телефона
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError(
                    'Неверное имя пользователя или пароль.',
                    code='invalid_login',
                )
            self.confirm_login_allowed(user)
            cleaned_data['user'] = user
        return cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'email', 'image')  # Поля для профиля

        labels = {
            'first_name': 'Имя',  # Указываем новое название для поля
            'image': 'Фото',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }