from django import forms
from .models import Email


class ContactForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['name', 'subject', 'e_mail', 'message']