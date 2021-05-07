from django.conf.urls import include
from django.urls import path
from secondapp import views


urlpatterns = [
    path('home2/',views.home2,name='home2'),
]
