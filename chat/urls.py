from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.map, name='chat')
]