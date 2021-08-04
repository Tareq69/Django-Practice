from django.conf.urls import url
from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.indexView2.as_view(), name='index'),
    path('musician_details/<pk>/', views.FighterDetail.as_view(), name='fighter_details'),
    path('add_fighters/', views.AddFighter.as_view(), name='add_fighters'),
    path('update_fighters/<pk>/', views.UpdateFighter.as_view(), name='update_fighters'),
    path('delete_fighters/<pk>/', views.DeleteFighter.as_view(), name='delete_fighter'),
]
