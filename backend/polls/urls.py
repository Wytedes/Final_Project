from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('movie/', views.get_movie_list, name='movie'),
    path('movie/categories/', views.get_movie_list_categories, name='categories'),
    path('movie/rate/', views.rate_movie.as_view(), name='rate'),
    path('movie/getrate/', views.get_rate_num.as_view(), name='getrate'),
]