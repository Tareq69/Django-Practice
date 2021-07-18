from django.shortcuts import render
from django.http import HttpResponse
from home.models import Musician, Album
from home import forms
from django.core.exceptions import ValidationError
# Create your views here.


def index(request):
    mlist = Musician.objects.order_by('first_name')
    dic={'T1':'List of musicians', 'm': mlist}
    return render(request, 'home/index.html',context= dic)  # Returning the index.html page from home folder of templates folder

def contact(request):
    dic={}
    return render(request, 'home/contact.html',context= dic ) # Returning the contact.html page from home folder of templates folder

def form(request):
    new_form = forms.Musician_form()

    if request.method == "POST":
        new_form = forms.Musician_form(request.POST)

    if new_form.is_valid():
        new_form.save(commit=True)
        return index(request)
    dic = {'tform': new_form}

    return render(request, 'home/form.html', context = dic)
