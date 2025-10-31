from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView 
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redredirect_authenticated_user = True
    

    def get_success_url(self):
        return reverse_lazy('profile')
    

class UserProfileView(DetailView):
    model = User
    template_name = "users/profile.html"
    context_object_name = "profile_user"