from django.urls import path
from . import views

urlpatterns = [
    path('', views.coders_home, name="coders_home"),
    path('<int:id>', views.coder_detail, name="coder_detail"),
]