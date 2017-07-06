
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    place = forms.CharField(max_length=20)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=13)
    message = forms.CharField(max_length=1000, required=True, widget=forms.Textarea)