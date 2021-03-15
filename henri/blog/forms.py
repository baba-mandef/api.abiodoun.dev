from django import forms
from henri.blog.models import Comment


class CommentForm(forms.ModelForm):
    # author_mail = forms.EmailField()
    class Meta:
        model = Comment
        fields = ('author_name', 'body', 'author_mail')
        labels = {
            'author_name': 'Votre nom',
            'author_mail': 'Votre mail (anonyme)',
            'body': 'Votre commentaire',
        }
