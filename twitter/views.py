from django.shortcuts import render
from django.shortcuts import HttpResponse
from twitter import models
import json
from twitter import Newest
from twitter import ScrapeData
from twitter import ProcessData
from twitter import PhraseCount
from twitter import FindLocation


datalist = []
def index(request):
    
    if request.method == 'POST':
        result = request.POST.get('data')
        print(result)
        result = Newest.getTweets(result)
        ScrapeData.getData(str(result))
        ProcessData.processData()
        PhraseCount.show()
        #PhraseCount.phrase()
        #FindLocation.getData()
        return HttpResponse(json.dumps({
                'result':result
            }))
    return render(request, 'homepage.html',{'data':datalist})

def chatbot(request):
    return  render(request, 'chatbot.html')