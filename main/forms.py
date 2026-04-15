from django import forms
from .models import QuickContact

class QuickContactForm(forms.ModelForm):
    class Meta:
        model = QuickContact
        fields = ['contact_info'] 
        widgets = {
            'contact_info': forms.TextInput(attrs={
                'class': 'form-control footer-input py-3 px-4',
                'placeholder': 'Ваш телефон або Email',
                'required': True
            })
        }