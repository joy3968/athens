from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import json

from django.views import View
from django.http import JsonResponse
from .models import customer_tbl

class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        customer_tbl(
            user_id = data['c_id'],
            user_pw = data['c_pw'],
        )

        if customer_tbl.objects.filter(user_id=data['c_id']).exists() == True:
            return JsonResponse({"message": "이미 존재하는 아이디입니다."}, status=401)

        else:
            customer_tbl.objects.create(user_id=data['c_id'], user_pw=data['c_pw'])
            return JsonResponse({"message": "회원으로 가입되셨습니다."}, status=200)
    def get(self, request):
        users = customer_tbl.object.values()
        return JsonResponse({"data" : list(users)}, status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        customer_tbl(
            user_id=data['c_id'],
            user_pw=data['c_pw'],
        )
        if customer_tbl.objects.filter(user_id=data['c_id'], user_pw=data['c_pw']).exists() == True:
            return JsonResponse({"message": "로그인에 성공하셨습니다."}, status=200)
        else:
            return JsonResponse({"message": "아이디나 비밀번호가 일치하지 않습니다."}, status=401)

    def get(self, request):
        user = customer_tbl.objects.values()
        return JsonResponse({"list": list(user)}, status=200)

#메인페이지 비로그인 상태 보이기
def mainpage(request):
    return render(request, 'mainpage/mainpage_body.html')

#마이페이지 Default 페이지, 비밀번호 인증
def mypagecheckpw(request):
    return render(request, 'mypage/checkpw.html')

#개인정보 수정 페이지
def mypageinsert(request):
    return render(request, 'mypage/information_insert.html')

# #마이페이지 출결현황
# def mypagecalendar(request):
#     return render(request, '/index.html')





# Create your views here.

