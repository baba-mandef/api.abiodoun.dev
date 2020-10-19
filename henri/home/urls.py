from django.urls import path
from henri.home import views

urlpatterns = [
    path('', views.home, name="home"),
]
