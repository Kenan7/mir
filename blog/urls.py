from django.urls import path
from blog.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:id>/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]