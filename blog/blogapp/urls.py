from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('videos/',views.vdo),

]
