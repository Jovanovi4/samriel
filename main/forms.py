from django import forms
from .models import Building, Seo, TypeChoise


class TypeForm(forms.ModelForm):
    class Meta:
        model = TypeChoise
        fields = [ 'type_choise', 'category' ]

        widgets = {
            'type_choise': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
        }





class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [
            'title',
            'top_description',
            'down_description',
            'deadline',
            'image',
            'image_slider',
            'jarlyk',
            'about_before_slide',
            'about_after_slide',
            'category',
            'video_name',
            'video',
            'location',
            'adres',
            'characteristic',
            'description2',
            'advantages',
            'deteil_description',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'top_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'down_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'deadline': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'image_slider': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'jarlyk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'about_before_slide': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'about_after_slide': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
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
            'description2': forms.Textarea(attrs={
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


class OldBuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [
            'title',
            'category',
            'square',
            'floor',
            'all_floor',
            'description1',
            'price',
            'image',
            'image_slider',
            'video',
            'location',
            'adres',
            'characteristic',
            'description2',
            'advantages',
            'deteil_description',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'square': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'floor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'all_floor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'deadline': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'image_slider': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
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
            'description2': forms.Textarea(attrs={
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
            'description1': forms.Textarea(attrs={
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