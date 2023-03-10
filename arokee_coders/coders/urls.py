from django.urls import path
from . import views

urlpatterns = [
    path('', views.coders_home, name="coders_home")
]