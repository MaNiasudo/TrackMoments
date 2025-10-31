from django.urls import path
from .views import TaskList ,TaskDetail, TaskCreate ,TaskUpdate , TaskDelete , CustomLoginView , register

from django.contrib.auth.views import LogoutView

path('login/', CustomLoginView.as_view(), name='login'),
path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
path('register/',register,name='register' )