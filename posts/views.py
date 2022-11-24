from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Post
from .models import Comment
from profiles.models import Profile

# Create your views here.
class PostDetailView(LoginRequiredMixin, DetailView):

    """ A DetailView class based view to render the post """

    template_name = 'posts/post.html'

    model = Post
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):

        """ Passing the post, the number of author's followers and if the current user follows the post author"""

        context = super().get_context_data(**kwargs)
        post = self.get_object()
        user_profile = Profile.objects.get(user=self.request.user)
        followers = post.author.followers.count()

        if user_profile.user in post.author.followers.all():
            follow = True
        else:
            follow = False
        context['follow'] = follow
        context['followers'] = followers
        print(context)
        return context

class PostCreateView(TemplateView):
    template_name = 'posts/create_post.html' 


def follow_unfollow(request):

    """ Add or remove the loged in user from the 'followers' field in the profile of the author """

    if request.method == 'POST':
        user_profile = Profile.objects.get(user=request.user)
        author_id = request.POST.get('author')
        author = Profile.objects.get(pk=author_id)

        print(author.followers.all())

        if user_profile.user in author.followers.all():
            # if the user is following the author, stop follow him
            author.followers.remove(user_profile.user)
            author.save()
        else:
            # if the user is not following the author, follow the author
            author.followers.add(user_profile.user)
            author.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('post_detail')

def to_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post')
        comment_content = request.POST.get('comment')
        
        comment_author = Profile.objects.get(user=request.user)
        post = Post.objects.get(pk=post_id)


        comment = Comment.objects.create(post=post, author=comment_author, content=comment_content)
        comment.save()
        print(comment)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('post_detail')
        
