from django.shortcuts import render, redirect
import bcrypt, random, string
from .forms import *
from django.utils import timezone
from admin.models import *

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
            return redirect('/teacher')

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
            return redirect('/teacher')

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
            return redirect('/teacher')

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


