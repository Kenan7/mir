from django.db import models
from django.contrib.auth import get_user_model

from core.models import GenericModelMixin

User = get_user_model()


class BlogArticle(GenericModelMixin):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def prepare_slug(self):
        self.slug = self.title.lower().replace(' ', '-')

        title_already_exists = BlogArticle.objects.filter(title=self.title).exists()
        if title_already_exists:
            self.slug += f'-{self.id}'

    def save(self, *args, **kwargs):
        self.prepare_slug()
        super().save(*args, **kwargs)