from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.begin, name='begin'),
    path('login/', views.login, name='login'),
]