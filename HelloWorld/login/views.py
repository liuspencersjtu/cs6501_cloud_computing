from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models
import json
from login import Newest

# Create your views here.
#user_list = []
datalist = []
def index(request):
    #return HttpResponse('Hello World!')
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        #temp = {'user' : username, 'pwd' : password}
        #user_list.append(temp)
        models.UserInfo.objects.create(user=username, pwd=password)

    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data' : user_list})
    '''
    if request.method == 'POST':
        result = request.POST.get('data')
        print(result)
        #temp = {'result':result}
        #datalist.append(temp)
        result = Newest.getTweets(result)
        return HttpResponse(json.dumps({
                'result':result
            }))
        #return render(request, 'homepage.html',{'data':datalist})
    #temp = {'result':'what'}
    #datalist.append(temp)
    return render(request, 'homepage.html',{'data':datalist})

def chatbot(request):
    return  render(request, 'chatbot.html')