from cmath import sqrt
from textwrap import indent
from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse, JsonResponse
from requests import session
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.views import View

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


class rate_movie(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        rate_user = request.session.get('user')
        rate_user = user.objects.all().filter(account=rate_user).first()
        
        to_movie = request.GET.get('movie')
        to_movie = Movie.objects.all().filter(title=to_movie).first()
        
        rate_num = request.GET.get('rate_num')
        
        rate_record = rate.objects.all().filter(user=rate_user, movie=to_movie).first()
        
        if rate_record is not None:
            rate_record.rate = rate_num
            rate_record.save()
            return JsonResponse({'success': True})
        
        if rate_user and to_movie and rate_num:
            rate_record = rate(user=rate_user, movie=to_movie, rate=rate_num)
            rate_record.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False}, status=202)
            
class get_rate_num(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        rate_user = request.session.get('user')
        rate_user = user.objects.all().filter(account=rate_user).first()
        
        to_movie = request.GET.get('movie')
        to_movie = Movie.objects.all().filter(title=to_movie).first()
        
        rate_record = rate.objects.all().filter(user=rate_user, movie=to_movie).first()
        
        if rate_record is not None:
            return JsonResponse({'rate_num': rate_record.rate})
        
        else:
            return JsonResponse({'rate_num': None}, status=202)

def getTogetherParam(movie1, movie2):
    movie1_user_rate = {}
    for m in movie1.object.all():
        for rate in m.rate_set.all():
            movie1_user_rate[rate.user.account] = rate.rate
            
    movie2_user_rate = {}
    for m in movie2.object.all():
        for rate in m.rate_set.all():
            movie2_user_rate[rate.user.account] = rate.rate
            
    together_user = movie1_user_rate.keys() & movie2_user_rate.keys()
    if len(together_user) == 0:
        return None
    
    movie1 = [movie1_user_rate[u] for u in together_user]
    movie2 = [movie2_user_rate[u] for u in together_user]
    return movie1, movie2

def getSimilar(movie1, movie2):
    movies = getTogetherParam(movie1, movie2)
    if movies == None:
        return 0
    
    fenzi = 0
    for i in range(0, len(movies[0])):
        fenzi += movies[0][i] * movies[1][i]
        
    fenmu1 = 0
    for i in range(0, len(movies[0])):
        fenmu += movies[0][i]^2
    fenmu1 = sqrt(fenmu1)
    
    fenmu2 = 0
    for i in range(0, len(movies[0])):
        fenmu += movies[1][i]^2
    fenmu2 = sqrt(fenmu2)
    
    result = fenzi / (fenmu1 * fenmu2)
        
class rate_predict(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        Costomer = request.session.get('user')
        All_Movie = Movie.objects.all()
        
        Movies_Seen = All_Movie.filter(rate__user__account=Costomer)
        Movies_Not_Seen = All_Movie.exclude(rate__user__account=Costomer)
        for Rating_Movie in Movies_Not_Seen:
            Movies_Similar = {}
            for Seen_Movie in Movies_Seen:
                S = getSimilar(Seen_Movie, Rating_Movie)
                