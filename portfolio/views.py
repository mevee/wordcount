from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'portfolio/index.html',{'hlo':'hlo friend how do you do'})

def home(request):
    return HttpResponse('<h1>you are home</h1>')

def projects(request):
    return HttpResponse('<h1>projects</h1>')

def about(request):
    return HttpResponse('<h1>about</h1>')
