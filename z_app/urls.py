# z_app
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('',views.home, name='home'),
<<<<<<< HEAD
   path('admin/', admin.site.urls),
   path('zsocialmedia/', include('zsocialmedia.urls')),
=======
<<<<<<< HEAD
   
=======
   path('tweets/<int:tweet_id>/comments/', views.comment_list, name='comment_list'),
   path('tweets/<int:tweet_id>/comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
   path('tweets/<int:tweet_id>/comments/new/', views.comment_create, name='comment_create'),
   path('tweets/<int:tweet_id>/comments/<int:comment_id>/edit/', views.comment_update, name='comment_update'),
   path('tweets/<int:tweet_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
>>>>>>> b67d6d7959c94ca1a83f8d5defd1b346a5f20740
>>>>>>> c84c93364a189d59d6d7592e73c81be6eeb2ce7a
]

