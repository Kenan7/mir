from django.shortcuts import render
from django.views.generic import RedirectView


class HomePageView(RedirectView):
    url = '/blog/articles/'
