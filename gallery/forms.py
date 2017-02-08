from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    subject = forms.CharField(max_length=70, required=True)
    e_mail = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def custom_validation(self):
        name = self.cleaned_data['name']
        name_length = len(name.split())

        if name_length < 1:
            raise forms.ValidationError('Sorry, name field cannot be empty')

        return name