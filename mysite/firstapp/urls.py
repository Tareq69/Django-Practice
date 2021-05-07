from django.conf.urls import include
from django.urls import path
from firstapp import views


urlpatterns = [
    path('',views.home,name='home'),
]
