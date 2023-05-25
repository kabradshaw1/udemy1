from django.urls import path
from .views import users, register, login, AuthenticatedUser, logout, PermissionsAPIView

urlpatterns = [
    path('users', users),
    path('register', register),
    path('login', login),
    path('user', AuthenticatedUser.as_view()),
    path('logout', logout),
    path('permission', PermissionsAPIView.as_view())
]
