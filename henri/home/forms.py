from django import forms


class Contact(forms.Form):
    author_mail = forms.EmailField(required=True, label='Email')
    mail_subject = forms.CharField(max_length=500, required=True, label='Objet')
    mail_content = forms.CharField(widget=forms.Textarea, required=True, label='Message')
