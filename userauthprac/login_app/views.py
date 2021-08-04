from django.shortcuts import render
from login_app.forms import UserForm,UserinfoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from login_app.models import Userinfo
from django.urls import reverse
from django.shortcuts import get_object_or_404


# Create your views here.



def index(request):
    dic = {}
    user_basic_info = None
    user_more_info = None
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = Userinfo.objects.get(pk=user_id)
        # user_more_info = get_object_or_404(Userinfo, pk=user_id)
    dic ={'user_basic_info':user_basic_info, 'user_more_info':user_more_info}
    return render(request, 'login_app/index.html', context=dic)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        userinfo_form = UserinfoForm(data=request.POST)

        if user_form.is_valid() and userinfo_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            userinfo = userinfo_form.save(commit=False)
            userinfo.user = user

            if 'profile_pic' in request.FILES:
                userinfo.profile_pic = request.FILES['profile_pic']

            userinfo.save()
            registered = True




    else:
        user_form = UserForm()
        userinfo_form = UserinfoForm()

    dic ={'user_form':user_form, 'userinfo_form':userinfo_form,'registered':registered}
    return render(request, 'login_app/register.html', context=dic)

def login_page(request):
    dic = {}
    return render(request, 'login_app/login.html', context = dic)

def user_login(request):
    dic={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('login_app:index'))
            else:
                return HttpResponse("Account is not active!!")

        else:
            return HttpResponse("username or password does not match!")
    else:
        return render(request, 'login_app/login.html', context=dic)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:index'))
