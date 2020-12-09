from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import userloginform
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.

def userlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)

        if user is not None :
            login(request, user)
            if user.is_staff == 1 :
                return redirect('/teacher')
            else:
                return redirect('/')

        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = userloginform()
        return render(request, 'login/login.html', {'form': form})

@login_required
def userlogout(request):
    logout(request)
    return redirect('/')



