# z_app
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name='home'),
   path('tweets/<int:tweet_id>/comments/', views.comment_list, name='comment_list'),
   path('tweets/<int:tweet_id>/comments/<int:pk>/', views.comment_detail, name='comment_detail'),
   path('tweets/<int:tweet_id>/comments/new/', views.comment_create, name='comment_create'),
]

