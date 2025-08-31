from django.urls import path
from hexlet_django_blog.article.views import (
    IndexView,
    ArticleView,
    ArticleFormView,
    ArticleFormEditView,
)


urlpatterns = [
#    path('', views.ArticleListView.as_view(), name='article_list'),
    path('', IndexView.as_view(), name='article_list'),
#    path('<int:article_id>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="articles_update"),
    path("<int:id>/delete/", ArticleFormDeleteView.as_view(), name="articles_delete"),
    path('<int:id>/', ArticleView.as_view(), name='article_detail'),
    path("create/", ArticleFormCreateView.as_view(), name="article_create"),
]
