from django.urls import path
from . import views

urlpatterns = [path('', views.index, name="index"),
 path('game', views.home, name="home")]
