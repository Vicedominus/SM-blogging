from django.urls import path
from .views import *

urlpatterns = [
    path('read/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('new_post/', PostCreateView.as_view(), name='write'),

    path('follow/', follow_unfollow, name='follow'),
    path('to_comment/', to_comment, name='to_comment'),
]