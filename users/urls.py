from django.urls import path
from .views import  CustomLoginView , register , UserProfileView, home_page

from django.contrib.auth.views import LogoutView

urlpatterns = [
path('', home_page, name='home_page' ),
path('login/', CustomLoginView.as_view(), name='login'),
path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
path('register/',register,name='register' ),
path("user/<int:pk>/", UserProfileView.as_view(), name="profile"),

]