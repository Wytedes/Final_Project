from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.begin, name='begin'),
    path('login/', views.login.as_view(), name='login'),
    path('registry/', views.registry.as_view(), name='registry'),
    path('logout/', views.logout.as_view(), name='logout'),
    path('logstatus/', views.get_login_status.as_view(), name='logstatus'),
]