from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def displayDateTime(request):
    import datetime
    now = datetime.datetime.now()
    return HttpResponse("<h1>Hello World</h1><br><h2>Current Date and Time is: "+str(now)+"</h2>")