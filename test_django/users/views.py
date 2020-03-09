from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.

def log_out(request):
    """注销用户"""
    logout(request)
    return HttpResponse("用户已注销")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('generic_view:list'))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
