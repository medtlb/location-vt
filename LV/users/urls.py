from django.urls import path
from knox import views as knox_views
from . import views
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('user/', views.get_user),
    path('login/', views.login),
    path('register/', views.register),
   # path('client/', views.ClientViewSet),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
  
]




