from django.contrib import admin
from blog.models import BlogArticle


@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published', 'created_at']
    list_filter = ('author', 'is_published')
    search_fields = ('title', 'author__username')
