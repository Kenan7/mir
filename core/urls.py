from django.urls import path
from core.views import (
    HomePageView,
    ContactView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]