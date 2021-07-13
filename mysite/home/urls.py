from django.conf.urls import url
from django.urls import path
from home import views

urlpatterns = [

    path('',views.index, name='index'), # mapping the index view
    # path('about/',views.About_us, name='about'),
    path('contact/',views.contact, name='contact') # mapping the contact view

]
