from django.urls import path
from . import views

urlpatterns = [
     path('count/',views.showresult,name='count'),
     path('',views.home,name='home'),
     path('about/',views.about,name='aboutus'),

]
