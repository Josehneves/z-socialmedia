# z_app
from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('',views.home, name='home'),
   path('profiles/', views.profiles, name='profiles'),
   path('profile/<int:pk>', views.profile, name='profile'),
   path('login/', views.login_user, name='login'),
   path('logout', views.logout_user, name='logout'),
   path('register', views.register_newuser, name='register'),
   path('tweet/', views.tweet_list, name='tweet_list'),
   path('tweet/<int:pk>/', views.tweet_detail, name='tweet_detail'),
   path('tweet_new/', views.tweet_new, name='tweet_new'),
   path('tweet/<int:pk>/edit/', views.tweet_edit, name='tweet_edit'),
   path('tweet/<int:pk>/delete/', views.tweet_delete, name='tweet_delete'),
   path('tweets/<int:tweet_id>/comments/', views.comment_list, name='comment_list'),
   path('tweets/<int:tweet_id>/comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
   path('tweets/<int:tweet_id>/comments/new/', views.comment_create, name='comment_create'),
   path('tweets/<int:tweet_id>/comments/<int:comment_id>/edit/', views.comment_update, name='comment_update'),
   path('tweets/<int:tweet_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
   path('comment/edit/<int:tweet_id>/<int:comment_id>/', views.comment_update, name='comment_update'),
   path('comment/delete/<int:tweet_id>/<int:comment_id>/', views.comment_delete, name='comment_delete'),

   
]
