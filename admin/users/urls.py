from django.urls import path
from .views import users, register, login, AuthenticatedUser, logout, PermissionsAPIView, RoleViewSet

urlpatterns = [
    path('users', users),
    path('register', register),
    path('login', login),
    path('user', AuthenticatedUser.as_view()),
    path('logout', logout),
    path('permission', PermissionsAPIView.as_view()),
    path('role', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
