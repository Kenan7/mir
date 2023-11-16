from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import BlogArticle
from django.shortcuts import get_object_or_404


class ArticleListView(ListView):
    model = BlogArticle
    paginate_by = 5
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = BlogArticle
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

    def get_object(self):
        return get_object_or_404(BlogArticle, id=self.kwargs['id'], slug=self.kwargs['slug'])