
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('admin_form', views.admin_form, name="admin_form"),
]
