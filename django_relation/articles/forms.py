from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        # article만 제외하고 넘기겠다
        exclude = ['article', 'user']