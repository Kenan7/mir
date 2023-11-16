import factory
from core.factories import UserFactory
from blog.models import BlogArticle


class BlogArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogArticle

    title = factory.Sequence(lambda n: f'Article {n}')
    content = factory.Faker('paragraph')
    author = factory.SubFactory(UserFactory)
