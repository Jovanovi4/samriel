from django import forms
from .models import FirstScreen, Contact, Sites, Choise, Image, SeoSites
from main.models import Building



class ChoiseForm(forms.ModelForm):
    class Meta:
        model = Choise
        fields = ['title', 'category', 'type',]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
        }
        
class ChoiseSelectForm(forms.ModelForm):
    selected_buildings = forms.ModelMultipleChoiceField(
        queryset=Building.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Позволяет использовать набор чекбоксов
        required=False,
    )

    class Meta:
        model = Choise
        fields = ['selected_buildings']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Фильтрация списка недвижимости по пользователю
            self.fields['selected_buildings'].queryset = Building.objects.filter(type_choise__user=user)




class FirstScreenForm(forms.ModelForm):
    class Meta:
        model = FirstScreen
        fields = [ 'image', 'name_company', 'title', 'category', 'prefix', 'price', 'question1', 'variants1',
                  'question2', 'variants2', 'question3', 'variants3', 'question4', 'variants4']
        
        widgets = {
            'name_company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'title': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'prefix': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'question1': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'variants1': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'question2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'variants2': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'question3': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'variants3': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'question4': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'variants4': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [ 'image_contacts', 'tg_link', 'whatsapp', 'description', 'number', 
                  'vk_link', 'instagram_link', 'youtube_link',
                 ]
        
        widgets = {
            'tg_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'whatsapp': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'vk_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'instagram_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'youtube_link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            
        }
        
        
class SitesForm(forms.ModelForm):
    class Meta:
        model = Sites
        fields = [ 'name_sites', 'number', 'decoding', 'text_under_number', 'link', 'icon', 'color'  ]

        widgets = {
            'icon': forms.HiddenInput(),
            'color': forms.HiddenInput(),
            'name_sites': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'decoding': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'text_under_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            
        }

    def __init__(self, *args, **kwargs):
        self.firstscreen = kwargs.pop('firstscreen', None)
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name and self.firstscreen:
            return self.firstscreen.name  # Замените title на нужное вам поле
        return name
    

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_icons']


class SeoSitesForm(forms.ModelForm):
    class Meta:
        model = SeoSites
        fields = ['name_seo', 'url_link_seo', 'deskription_seo', 'key_word_seo']

        widgets = {
            'name_seo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'url_link_seo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите ссылку'
            }),
            'deskription_seo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'key_word_seo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
        }