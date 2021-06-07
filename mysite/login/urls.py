from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', views.create_account, name='signup'),
    path('home/', views.dashboard, name='dashboard'),
]
