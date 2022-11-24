from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.
class UserCreationView(FormView):
    template_name = 'users/join.html'

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        # save the user
        user = form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'users/login.html'

    form_class = CustomAuthenticationForm
    next_page = reverse_lazy('feed')
    redirect_authenticated_user = True





