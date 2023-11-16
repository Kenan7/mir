from django.test import TestCase
from django.urls import reverse
from blog.factories import BlogArticleFactory
from core.factories import UserFactory


class ArticleListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = UserFactory()
        for i in range(10):
            BlogArticleFactory(author=user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('article-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('article-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['articles']), 5)


class ArticleListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = UserFactory()
        for i in range(10):
            BlogArticleFactory(author=user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('article-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('article-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['articles']), 5)
