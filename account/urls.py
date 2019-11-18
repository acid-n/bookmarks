from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Определенные ранее обработчики
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
]
