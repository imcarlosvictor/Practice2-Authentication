from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.create_account, name='login'),
    path('user/', views.user_login, name='dashboard'),
]
