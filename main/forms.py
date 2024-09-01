from django import forms
from .models import Building, Seo, TypeChoise, Image, Plans


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

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        # Используем стандартную обработку, но поддерживаем несколько файлов
        if isinstance(data, (list, tuple)):
            result = [super().clean(d, initial) for d in data]
        else:
            result = [super().clean(data, initial)]
        return result


class ImagePlansForm(forms.ModelForm):
    image_plans = MultipleFileField(
        label="Планировки",
        required=False
    )
    class Meta:
        model = Image
        fields = ['image_plans']


class ImageForm(forms.ModelForm):
    image_s = MultipleFileField(
        label="Изображения для слайдера",
        required=False
    )

    class Meta:
        model = Image
        fields = ['image_s']



class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [
            'title',
            'top_description',
            'down_description',
            'deadline',
            'jarlyk',
            'image',
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
            'jarlyk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
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
            'image',
            'description1',
            'price',
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
            'image': forms.ClearableFileInput(attrs={
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


class PlansForm(forms.ModelForm):
    plan_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Plans
        fields = ['type_building', 'quanty_room', 'total_area_from', 'total_area_upto',
                  'price_from', 'price_upto', 'description',]
        
        widgets = {
            'type_building': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Студии, 1-комнатные, 2-комнатные'
            }),
            'quanty_room': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1, 2, 3'
            }),
            'total_area_from': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '42,5'
            }),
            'total_area_upto': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '42,5'
            }),
            'price_from': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '3000000'
            }),
           'price_upto': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '3000000'
            }),
           'description': forms.Textarea(attrs={
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