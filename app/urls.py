
from django.urls import path,include
from app import views

urlpatterns = [
    path("",views.index),
    path("about",views.about),
    path("gallery",views.gallery),
  
]