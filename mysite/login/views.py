from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import user
from django.views.decorators.csrf import csrf_exempt

def begin(request):
    return render(request, 'begin.html')

@csrf_exempt
def login(request):
    acc = request.POST.get('account')
    pwd = request.POST.get('password')
    print(request.POST)
    getAllUser = user.objects.all()
    getUser = getAllUser.filter(account=acc)
    if len(getUser) > 0:
        getUser = getUser[0]
        if getUser.password == pwd:
            return JsonResponse({'username': acc, 'pwd': pwd})
        else:
            return HttpResponse("Account or password is incorrect!")
    else:
        return HttpResponse("Account not exits!")
    
