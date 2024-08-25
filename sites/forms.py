from django import forms
from .models import FirstScreen, Contact, Sites, Choise



class ChoiseForm(forms.ModelForm):
    class Meta:
        model = Choise
        fields = ['title', 'category', 'type',]
        



class FirstScreenForm(forms.ModelForm):
    class Meta:
        model = FirstScreen
        fields = [ 'image', 'name', 'title', 'category', 'prefix', 'price', 'question1', 'variants1',
                  'question2', 'variants2', 'question3', 'variants3', 'question4', 'variants4']
        