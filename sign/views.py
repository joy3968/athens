from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import bcrypt


# Create your views here.

from django.http import HttpResponse


def sign(request):
    return render(request, 'sign/select_type.html')

def s_tos(request):
    return render(request, 'sign/S_TOS.html')
def p_tos(request):
    return render(request, 'sign/P_TOS.html')
def t_tos(request):
    return render(request, 'sign/T_TOS.html')