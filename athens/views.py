from django.contrib.auth import views, models, login
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import CreateView
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
import bcrypt, random, string, json, traceback


# 회원가입 폼 가져오기
from .forms import *

# notice_tbl 가져오기
from .models import *

# notice_index.html 페이지를 부르는 notice_index 함수
def notice_index(request):
    # 공지사항 목록 불러오기
    noticelist = notice_tbl.objects.order_by('-notice_date')

    # 페이징
    page = request.GET.get('page','1') # 페이지
    paginator = Paginator(noticelist,5) # 페이지당 5개
    page_obj = paginator.get_page(page)
    context = {'noticelist':page_obj}

    # notice_list.html을 열 때 , 모든 notice인 noticelist도 가져옵니다.
    return render(request, 'notice/notice_index.html',context)

# notice_content.html 페이지를 부르는 notice_content 함수
def notice_content(request,pk):
    # 공지사항 pk이용해서 찾기
    content = notice_tbl.objects.get(pk=pk)
    # notice_content.html을 열 때, 찾은 게시글을 content로 받는다.
    return render(request,'notice/notice_content.html',{'content':content})

# 학생 회원가입

def student_sign_up(request):
    if request.method == "POST":
        form = studentsignupform(request.POST)
        if form.is_valid():
            customer_tbl = form.save(commit=False)
            customer_tbl.c_join = timezone.now()
            customer_tbl.c_state = True

            # 비밀번호 암호화
            customer_tbl.c_pw = makeHashPassword(customer_tbl.c_pw)

            # c_code 생성

            random_code = ''
            string_code = string.ascii_letters + string.digits

            for i in range(6):
                random_code += random.choice(string_code)

            customer_tbl.c_code = random_code
            # db에 정보 저장
            customer_tbl.save()
            return redirect('/')

    else:
        form = studentsignupform()

    return render(request,'sign_up/c_signup.html',{'form':form})

# 학부모 회원가입

def parent_sign_up(request):
    if request.method == "POST":
        form = parentsignupform(request.POST)
        if form.is_valid():
            customer_tbl = form.save(commit=False)
            customer_tbl.c_join = timezone.now()
            customer_tbl.c_state = True

            # 비밀번호 암호화
            customer_tbl.c_pw = makeHashPassword(customer_tbl.c_pw)

            # db에 정보 저장
            customer_tbl.save()
            return redirect('/')

    else:
        form = parentsignupform()

    return render(request,'sign_up/c_signup.html',{'form':form})

# 선생님 회원가입

def teacher_sign_up(request):
    if request.method == "POST":
        form = teachersignupform(request.POST,request.FILES)
        if form.is_valid():
            teacher_tbl = form.save(commit=False)
            teacher_tbl.t_join = timezone.now()
            teacher_tbl.t_state = True

            # 비밀번호 암호화
            teacher_tbl.t_pw = makeHashPassword(teacher_tbl.t_pw)

            # db에 정보 저장
            teacher_tbl.save()
            return redirect('/')

    else:
        form = teachersignupform()

    return render(request,'sign_up/t_signup.html',{'form':form})

# 비밀번호 암호화
def makeHashPassword(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'),salt)
    return hashed.decode()

# 비밀번호 찾기 / 로그인 시 비밀번호 확인
def isPasswordCheck(hashed,password):
    return bcrypt.checkpw(password.encode('utf-8'),hashed.encode())

