from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from .forms import LectureForm

# 메인 화면
def index(request):
    day = timezone.now()
    context = {'day' : day}

    return render(request, 'admin/main.html', context)

# 로그인
def login(request):
    return render(request, 'admin/login.html')

# 현재 선생님
def teacher_in(request):
    teacher_list = teacher_tbl.objects.order_by('-t_join')
    context = {'teacher_list': teacher_list}

    return render(request, 'admin/contact-directory.html', context)

# 퇴사 선생님
def teacher_out(request):

    teacher_list = teacher_tbl.objects.order_by('-t_join')
    day = timezone.now()
    context = {'teacher_list': teacher_list, 'day' : day}

    return render(request, 'admin/datatable.html', context)

# 선생님 상세
def teacher_detail(request, teacher_tbl_t_no):
    """
    선생님 상세
    """
    teacher_info = teacher_tbl.objects.get(pk = teacher_tbl_t_no)
    context = {'teacher_info' : teacher_info}

    return render(request, 'admin/teacher-detail.html', context)

# 수강생
def student_in(request):
    customer_list = customer_tbl.objects.order_by('-c_join')
    context = {'customer_list' : customer_list}

    return render(request, 'admin/student-in.html', context)

# 퇴원생
def student_out(request):

    customer_list = customer_tbl.objects.order_by('-c_join')
    context = {'customer_list': customer_list}

    return render(request, 'admin/student-out.html', context)

# 학생 상세
def student_detail(request):
    return render(request, 'admin/student-detail.html')

# 강의 등록
def lecture_create(request):
    """
    lecture 등록
    """
    if request.method == 'POST':
        print(111,request.POST)
        print(222,request.FILES['l_img'])


        form = LectureForm(request.POST)
        if form.is_valid():
            lecture_tbl = form.save(commit=False)
            lecture_tbl.l_img = request.FILES['l_img']
            lecture_tbl.save()

            return redirect('admin:index')

    else:
        form = LectureForm()

    teacher_list : teacher_tbl.objects.order_by(-'t_join')
    context = {'form' : form}

    return render(request, 'admin/lecture_form.html', context)

# 학부모 목록
def parents_list(request):
    customer_list = customer_tbl.objects.order_by('-c_join')

    # customer_tbl.objects.get(pk = )

    context = {'customer_list': customer_list}



    return render(request, 'admin/parent_list.html', context)

# Create your views here.