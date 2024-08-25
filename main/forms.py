from django import forms
from .models import Building, Seo


class TypeForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [ 'type' ]



class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [
            'title', 'top_description', 'down_description', 'deadline', 'jarlyk', 
            'about_before_slide', 'about_after_slide', 'category', 'video_name', 'video', 
            'location', 'adres', 'characteristic', 'description', 'advantages', 'deteil_description',
            'image', 'type'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'top_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 3
            }),
            'down_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 3
            }),
            'deadline': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите срок сдачи'
            }),
            'jarlyk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите старт продаж'
            }),
            'about_before_slide': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 3
            }),
            'about_after_slide': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 3
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'video_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'video': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'adres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'characteristic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'advantages': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'deteil_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }


class OldBuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [
            'title', 'top_description', 'down_description', 'about_before_slide', 
            'about_after_slide', 'square', 'floor', 'all_floor', 'price', 'image', 'category',
            'location', 'adres', 'characteristic', 'description', 
            'advantages', 'deteil_description', 'type'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'top_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 3
            }),
            'down_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 3
            }),
            'about_before_slide': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 3
            }),
            'about_after_slide': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 3
            }),
            'square': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите площадь'
            }),
            'floor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите этаж'
            }),
            'all_floor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите кол-во этажей'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите цену'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'adres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'characteristic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'advantages': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'deteil_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
        }


        
class SeoForm(forms.ModelForm):
    class Meta:
        model = Seo
        fields = ['name', 'url_link', 'deskription_seo', 'key_word']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'url_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите ссылку'
            }),
            'deskription_seo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'key_word': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
        }