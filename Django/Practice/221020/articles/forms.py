from .models import Article, Comment
from django import forms

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('user',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('article',)