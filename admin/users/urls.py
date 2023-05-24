from django.urls import path
from .views import users, register, login

urlpatterns = [
    path('user/', users),
    path('register/', register),
    path('login/', login),
]
