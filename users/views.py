from django.shortcuts import render , redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView 
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import UserRegisterForm , UserUpdateForm
from django.contrib import messages



def home_page(request):
     if request.method == 'POST':
        return render(request, 'users/home_page.html')
     else:
        return render(request, 'users/home_page.html')
     
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redredirect_authenticated_user = True
    

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})
    

class UserProfileView(DetailView, LoginRequiredMixin):
    model = User
    template_name = "users/profile.html"
    context_object_name = "profile_user"


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"Your account has been created! You can login now")
                return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})    
        

