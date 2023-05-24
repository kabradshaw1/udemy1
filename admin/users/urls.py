from django.urls import path
from .views import user, register

urlpatterns = [
    path('user/', user),
    path('register/', register)
]
