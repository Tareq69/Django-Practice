from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/',include('home.urls')),
]
