from textwrap import indent
from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Question, Movie
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def get_movie_list(request):
    movie_list = Movie.objects.all()
    movie_object_list = [{
            'title': movie.title,
            'oth_title': movie.oth_title,
            'category': movie.category,
            'rating_num': movie.rating_num,
            'picture': movie.picture
        } for movie in movie_list]
    category = request.GET.get('category', '全部')
    if category!='全部':
        movie_object_list = [movie for movie in movie_object_list if category in movie['category']]
    return JsonResponse(movie_object_list, safe=False, json_dumps_params={'ensure_ascii':False, 'indent':4})

@csrf_exempt
def get_movie_list_categories(request):
    movie_list = Movie.objects.all()
    movie_category_dict = {}
    
    # 统计类别频率
    for movie in movie_list:
        for category in movie.category.split(' '):
            if category == '剧情':
                continue
            elif movie_category_dict.get(category) is not None:
                movie_category_dict[category] += 1
            else:
                movie_category_dict[category] = 1
                
    categories_sort_by_frequency = sorted(movie_category_dict.items(), key=lambda x: x[1], reverse=True)
    
    return JsonResponse(categories_sort_by_frequency, safe=False, json_dumps_params={'ensure_ascii':False, 'indent':4})
