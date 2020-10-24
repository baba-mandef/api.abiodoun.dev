from django import forms
from henri.blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name', 'body', 'author_mail')
        labels = {
            'author_name': 'Votre nom',
            'author_mail': 'Votre mail(anonyme)',
            'body': 'Votre commentaire',
        }
