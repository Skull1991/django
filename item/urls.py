from django.urls import path
from item import views

urlpatterns = [
    path("",views.index),
    path("save/",views.save),
    path("create/",views.create),
]