from django import forms
from django.conf import settings
from .models import ContactTable
from django.forms import ModelForm


class ContactForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),required=True)
    message = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model = ContactTable
        fields = ('firstname','email','message')