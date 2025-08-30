from django import forms  # Импортируем формы Django
from django.forms import ModelForm
from .models import Article, ArticleComment


# Создание формы "вручную"
class CommentArticleForm(forms.Form):
    content = forms.CharField(label="Комментарий", max_length=200)  # Текст комментария

# Создание формы с помощью встроенного генератора
class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content"]

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]
