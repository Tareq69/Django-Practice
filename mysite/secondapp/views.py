from django.shortcuts import render
from django.http import HttpResponse



def home2(request):
    return HttpResponse("<h1>This is homepage2</h1> <a href='/firstapp/home'>GO to homepage1</a> ")
