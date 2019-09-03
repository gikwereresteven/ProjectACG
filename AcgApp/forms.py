from django import forms
from .models import  ContactTable


class ContactForm(forms.ModelForm):
    firstname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'size':'30','class':'inputText'}))
    email= forms.EmailField( max_length=100,widget=forms.TextInput(attrs={'size':'30','class':'inputText'}))
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":30}))
    class Meta:
        model:ContactTable
        fields = ('firstname','email','message')