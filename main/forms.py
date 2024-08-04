from django import forms
from .models import Building


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [
            'title', 'top_description', 'down_description', 'deadline', 'jarlyk', 
            'about_before_slide', 'about_after_slide', 'category', 'video_name', 'video', 
            'location', 'adres', 'characteristic', 'description', 'advantages', 'deteil_description',
            'square', 'floor', 'all_floor', 'price' , 'image'
        ]



class OldBuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [
            'title', 'top_description', 'down_description', 'deadline', 'jarlyk', 
            'about_before_slide', 
        ]




#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),
#             'top_description': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': '',
#                 'rows': 3
#             }),
#             'down_description': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': '',
#                 'rows': 3
#             }),
#             'deadline': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите срок сдачи'
#             }),
#             'jarlyk': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Укажите старт продаж'
#             }),
#             'about_before_slide': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': '',
#                 'rows': 3
#             }),
#             'about_after_slide': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': '',
#                 'rows': 3
#             }),
#             'category': forms.Select(attrs={
#                 'class': 'form-control',
#             }),
#             'video_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': ''
#             }),

#             'video': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': ''
#             }),

#             'location': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': ''
#             }),

#             'adres': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': ''
#             }),

#             'characteristic': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': ''
#             }),

#             'description': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': ''
#             }),

#             'advantages': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': ''
#             }),

#             'deteil_description': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': ''
#             }),

#         }

# class OldBuildingForm(forms.ModelForm):
#     class Meta:
#         model = Old_Buildings
#         fields = [
#             'title', 'category', 'square', 'floor', 'all_floor', 'price', 'description',
#             'video', 'location', 'adres', 'characteristic', 'deteil_description'
    
    
#         ]
#         widgets = {

#             'title': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),

#             'category': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),
            
#             'square': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),

#             'floor': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),

#             'all_floor': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),

#             'price': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),

#             'description': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),

#             'video': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),    

#             'location': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),

#             'adres': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),

#             'characteristic': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),

#             'deteil_description': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите название'
#             }),

#         }
        


