from django.urls import path
from .views import users, register

urlpatterns = [
    path('user/', users),
    path('register/', register)
]
