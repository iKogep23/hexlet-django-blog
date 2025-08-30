from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
#    path('', views.ArticleListView.as_view(), name='article_list'),
    path('', views.IndexView.as_view(), name='article_list'),
#    path('<int:article_id>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<int:id>/', views.ArticleView.as_view(), name='article_detail'),
    path("create/", views.ArticleFormCreateView.as_view(), name="article_create"),
]
