from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("<h1>article</h1>")


def index(request):
    return render(
        request,
        "index.html",
        context={
            'who': 'Article',
        }
    )

# Create your views here.
