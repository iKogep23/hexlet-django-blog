# hexlet_django_blog/views.py
# from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        tags = ["обучение", "программирование", "python", "oop"]
        context = super().get_context_data(**kwargs)
        context["tags"] = tags
        return context
