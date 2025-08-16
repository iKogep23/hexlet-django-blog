from django.shortcuts import render
from django.http import HttpResponse
from hexlet_django_blog.views import IndexView


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

# Create your views here.
