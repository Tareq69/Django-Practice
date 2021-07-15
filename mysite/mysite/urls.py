from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),# Mapping the urls of home app's url.py
]
