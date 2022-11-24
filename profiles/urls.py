from django.urls import path
from .views import *

urlpatterns = [
    path('<str:username>/', ProfileTemplateView.as_view(), name='profile'),
]