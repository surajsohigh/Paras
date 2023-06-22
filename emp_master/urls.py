from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('empMaster', views.empMaster, name='empMaster'),
    path('home', views.home, name='home'),



]