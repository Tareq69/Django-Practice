from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    dic={}
    return render(request, 'home/index.html',context= dic)  # Returning the index.html page from home folder of templates folder

def contact(request):
    dic={}
    return render(request, 'home/contact.html',context= dic ) # Returning the contact.html page from home folder of templates folder
#
# def About_us(request):
#     return HttpResponse("<h1>About us</h1> <a href='/home/contact'>Contact us </a> ")
