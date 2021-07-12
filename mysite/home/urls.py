from django.conf.urls import url
from django.urls import path
from home import views

urlpatterns = [

    path('index/',views.index, name='index'),
    path('about/',views.About_us, name='about'),
    path('contact/',views.contact, name='contact')

]
