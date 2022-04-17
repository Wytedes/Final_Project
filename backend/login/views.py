import json
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import user
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from polls.models import Movie
def begin(request):
    acc = request.session.get('user')
    return render(request, 'begin.html', {'user': acc})
""" 
@csrf_exempt
def login(request):
    acc = request.POST.get('account')
    pwd = request.POST.get('password')
    # jsn = request.body.decode('utf-8')
    # jsn = json.loads(jsn)
    # print(jsn)
    # print(request.POST)
    # print(dir(request))
    getAllUser = user.objects.all()
    getUser = getAllUser.filter(account=acc).filter(password=pwd).first()
    print(getAllUser)
    if getUser:
        return JsonResponse({'username': acc, 'pwd': pwd, 'success': True})
    else:
        return JsonResponse({'username': acc, 'pwd': pwd, 'success': False})
   """  

class registry(View):
    def post(self, request):
        acc = request.POST.get('account')
        pwd = request.POST.get('password')
        
        AllUser = user.objects.all()
        getUser = AllUser.filter(account=acc).first()
        
        if getUser:  # 如果存在相同的用户
            return JsonResponse({'success':False}, status=202)
        else:
            request.session['is_login'] = True
            request.session['user'] = acc
            new_user = user(account=acc, password=pwd)
            new_user.save()
            return JsonResponse({'success':True}) 
        
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class get_login_status(View):
    def get(self, request):
        status = {}
        if request.session.get('is_login'):
            status['user'] = request.session['user']
            return JsonResponse(status, safe=False, json_dumps_params={'ensure_ascii':False, 'indent':4}, status=200)
        else :
            return JsonResponse(status, status=202)
    
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class login(View):
    def post(self, request):
        acc = request.POST.get('account')
        pwd = request.POST.get('password')
        # jsn = request.body.decode('utf-8')
        # jsn = json.loads(jsn)
        # print(jsn)
        # print(request.POST)
        # print(dir(request))
        getAllUser = user.objects.all()
        getUser = getAllUser.filter(account=acc).filter(password=pwd).first()
        
        if getUser:
            request.session['is_login'] = True
            request.session['user'] = acc
            return JsonResponse({'username': acc, 'pwd': pwd, 'success': True})
            # return redirect('/')
        else:
            return JsonResponse({'username': acc, 'pwd': pwd, 'success': False}, status=202)
        
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class logout(View):
    def get(self, request):
        request.session.flush()
        return redirect('/')
        
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
