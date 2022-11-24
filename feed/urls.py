from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('', FeedTemplateView.as_view(), name='feed'),
]