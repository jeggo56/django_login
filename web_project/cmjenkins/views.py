import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Hello,django')

def hello_there(request):
    return render(
        request,
        'cmjenkins/hello_there.html',

    )