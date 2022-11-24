from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from posts.models import Post

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'feed/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all()[:5]
        return context

class FeedTemplateView(LoginRequiredMixin, ListView):
    template_name = 'feed/feed.html'

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
