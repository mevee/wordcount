from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('projects/',views.projects),
    path('about/',views.about),
]
