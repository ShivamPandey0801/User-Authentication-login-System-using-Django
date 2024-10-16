from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def home(request):
    return render(request, 'a.html', {'titles':'', 'link':'http://127.0.0.1:8000/'})

def profile(request):
    return render(request, 'a.html', {'titles':'Profile Page', 'link':'http://127.0.0.1:8000/'})

def expression(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+2*b
    return render(request,'output.html', {'result':c})