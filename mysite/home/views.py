from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>I am from first app</h1> <a href='/home/about/'>About us</a>")

def contact(request):
    return HttpResponse("<h1>Contact us</h1> <a href='/home/index/'>Home</a>")

def About_us(request):
    return HttpResponse("<h1>About us</h1> <a href='/home/contact'>Contact us </a> ")
