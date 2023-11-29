# z_app
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('',views.home, name='home'),
   path('admin/', admin.site.urls),
   path('zsocialmedia/', include('zsocialmedia.urls')),
]
