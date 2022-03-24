from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Question, Movie

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    response = f'You\'re looking at question {question_id}'
    return HttpResponse(response)

def results(request, question_id):
    response = f'You\'re looking at the results of question {question_id}'
    return HttpResponse(response)

def vote(request, question_id):
    response = f'You\'re voting on question {question_id}'
    return HttpResponse(response)

def get_movie_list(request):
    movie_list = Movie.objects.all()
    movie_object_list = [{
            'title': movie.title,
            'oth_title': movie.oth_title,
            'category': movie.category,
            'rating_num': movie.rating_num,
            'picture': movie.picture
        } for movie in movie_list]
    return JsonResponse(movie_object_list, safe=False)
