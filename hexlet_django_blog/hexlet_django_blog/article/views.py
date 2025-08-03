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


class ArticleView(IndexView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "Article"
        return context

# Create your views here.
