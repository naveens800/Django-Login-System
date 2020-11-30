from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'loginRegister/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get(['username'])
        password = request.POST.get(['password'])
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("You are not an active User")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")

    else:
        return render(request, 'loginRegister/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


def user_register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('Found it')
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
                return redirect('user_login')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        context = {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered}
        return render(request, 'loginRegister/register.html', context)
