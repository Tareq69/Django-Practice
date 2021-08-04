from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from first_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls')),
]
