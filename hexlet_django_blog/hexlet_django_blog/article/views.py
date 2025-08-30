from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import View
from hexlet_django_blog.views import IndexView

from hexlet_django_blog.article.models import Article
from .forms import CommentArticleForm
from .models import ArticleComment


#def index(request):
#    return HttpResponse("<h1>article</h1>")


#def index(request):
#    return render(
#        request,
#        "index.html",
#        context={
#            'who': 'Article',
#        }
#    )


#class ArticleView(IndexView):
#    template_name = "index.html"
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context["who"] = "Article"
#        return context


ARTICLES = [
    {"id": 1, "title": "Первая статья"},
    {"id": 2, "title": "Вторая статья"},
    {"id": 3, "title": "Третья статья"},
    {"id": 4, "title": "Четвертая статья"},
    {"id": 5, "title": "Пятая статья"},
    {"id": 6, "title": "Шестая статья"},
    {"id": 7, "title": "Седьмая статья"},
    {"id": 8, "title": "Восьмая статья"},
    {"id": 9, "title": "Девятая статья"},
    {"id": 10, "title": "Десятая статья"},
]


class ArticleListView(IndexView):
    template_name = "articles/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = ARTICLES
        return context


class ArticleDetailView(IndexView):
    template_name = "articles/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = self.kwargs['article_id']
        article = next((a for a in ARTICLES if a['id'] == article_id), None)
        context['article'] = article
        return context


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:10]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/show.html',
            context={
                "article": article,
            }
        )


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "article/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():  # Если данные формы корректные, то сохраняеем
            form.save()
            return redirect('articles')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})


class CommentArticleView(View):
    # если метод POST, то мы обрабатываем данные
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)  # Получаем данные из запроса
        if form.is_valid():  # Проверяем данные на корректность
            comment = ArticleComment(
                content=form.cleaned_data["content"],  # Получаем очищенные данные из поля content
            )  # и создаем новый комментарий
            comment.save()

    # если метод GET, то создаем пустую форму
    def get(self, request, *args, ** kwargs):
        form = CommentArticleForm()  # Создаем экземпляр нашей формы
        return render(
            request, "comment.html", {"form": form}
        )  # Передаем нашу форму в контексте


class ArticleCommentFormView(View):
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данные формы на корректность
#            form.save()  # Сохраняем форму, но можно вместо этого дополнительно обработать данные формы
            comment = form.save(commit=False)  # Получаем заполненную модель
            # Дополнительно обрабатываем модель чрез стороннюю функцию, которую нужно подключить
            # либо путем импорта из сторонней библиотеки (например, сервис akismet:
            # from akismet import check_for_spam), либо самостоятельной реализации:
            # from .utils import check_for_spam
#            comment.content = check_for_spam(form.data["content"])
            comment.save()

# Create your views here.
