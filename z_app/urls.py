# z_app
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name='home'),
   path('profiles/', views.profiles, name='profiles'),
   path('profile/<int:pk>', views.profile, name='profile'),
   path('login/', views.login_user, name='login'),
   path('logout', views.logout_user, name='logout'),
   path('register', views.register_newuser, name='register'),
]
