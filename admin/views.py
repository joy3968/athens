from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from .forms import *
from django.contrib.auth import authenticate, login, logout

# 메인 화면
def index(request):
    day = timezone.now()
    context = {'day' : day}

    return render(request, 'admin/main.html', context)

# 사용자페이지 이미지
def userpage(request):
    return render(request, 'admin/userpage.html')

# 현재 선생님
def teacher_in(request):
    teacher_list = teacher_tbl.objects.order_by('-t_join')
    context = {'teacher_list': teacher_list}

    return render(request, 'admin/teacher_in.html', context)

# 퇴사 선생님
def teacher_out(request):
    if request.method == 'POST':
        print(request.POST)
        teacher_info = teacher_tbl.objects.get(pk=request.POST['t_no'])
        teacher_info.t_state = True
        teacher_info.t_out = None
        teacher_info.save()

    teacher_list = teacher_tbl.objects.order_by('-t_join')
    day = timezone.now()
    context = {'teacher_list': teacher_list, 'day' : day}

    return render(request, 'admin/teacher_out.html', context)

# # 선생님 상세
# def teacher_detail(request, teacher_tbl_t_no):
#     """
#     선생님 상세
#     """
#     teacher_info = teacher_tbl.objects.get(pk = teacher_tbl_t_no)
#     lecture_list = lecture_tbl.objects.order_by('-l_no')
#     context = {'teacher_info' : teacher_info, 'lecture_list' : lecture_list}
#
#     return render(request, 'admin/teacher-detail.html', context)

# 선생님 상세
def teacher_detail(request, teacher_tbl_t_no):
    """
    선생님 상세
    """

    if request.method == 'POST':
        # print(123123,request.POST['1'])
        # print(123,request.POST['버튼'])
        if request.POST['버튼'] == '1':
            # print(123123,teacher_tbl_t_no)
            teacher_info = teacher_tbl.objects.get(pk = teacher_tbl_t_no)
            # print(12345,teacher_info)
            teacher_info.t_state = False
            teacher_info.t_out = timezone.now()
            # teacher_tbl.t_sate = False
            teacher_info.save()
            # print('ggk',111)

            lecture_list = lecture_tbl.objects.order_by('-l_no')
            # teacher_info = teacher_tbl.objects.get(pk=teacher_tbl_t_no)

            context = {'teacher_info' : teacher_info, 'lecture_list' : lecture_list}

            return render(request, 'admin/teacher-detail.html', context)

        elif request.POST['버튼'] == '2':
            print(request.POST)
            teacher_info = teacher_tbl.objects.get(pk=teacher_tbl_t_no)
            teacher_info.t_text = request.POST['t_text']
            teacher_info.save()

            lecture_list = lecture_tbl.objects.order_by('-l_no')
            # teacher_info = teacher_tbl.objects.get(pk=teacher_tbl_t_no)

            context = {'teacher_info': teacher_info, 'lecture_list': lecture_list}

            return render(request, 'admin/teacher-detail.html', context)





    teacher_info = teacher_tbl.objects.get(pk=teacher_tbl_t_no)
    lecture_list = lecture_tbl.objects.order_by('-l_no')
    context = {'teacher_info': teacher_info, 'lecture_list': lecture_list}

    return render(request, 'admin/teacher-detail.html', context)

# 수강생
def student_in(request):
    customer_list = customer_tbl.objects.order_by('-c_join')
    context = {'customer_list' : customer_list}

    return render(request, 'admin/student-in.html', context)

# 퇴원생
def student_out(request):
    if request.method == 'POST':
        print(request.POST)
        customer_info = customer_tbl.objects.get(pk=request.POST['c_no'])
        customer_info.c_state = True
        customer_info.c_out = None
        customer_info.save()


    customer_list = customer_tbl.objects.order_by('-c_join')
    context = {'customer_list': customer_list}

    return render(request, 'admin/student-out.html', context)

# 학생 상세
def student_detail(request, c_no):
    if request.method == 'POST':
        # print(123123,request.POST['1'])
        # print(123,request.POST['버튼'])
        if request.POST['버튼'] == '1':
            # print(123123,teacher_tbl_t_no)
            customer_info = customer_tbl.objects.get(pk = c_no)
            customer_info.c_state = False
            customer_info.c_out = timezone.now()
            customer_info.save()

            lecture_list = lecture_tbl.objects.order_by('-l_no')

            context = {'customer_info' : customer_info, 'lecture_list' : lecture_list}
            return render(request, 'admin/student-detail.html', context)

    student_info = customer_tbl.objects.get(pk=c_no)
    context = {'customer_info': student_info}

    return render(request, 'admin/student-detail.html', context)

# # 강의 등록
# def lecture_create(request):
#     """
#     lecture 등록
#     """
#     if request.method == 'POST':
#         # print(111,request.POST)
#         print(request.POST)
#
#         # print(222,request.FILES['l_img'])
#         form = LectureForm()
#         # print(form.clean())
#         # if form_teacher.is_valid():
#         #
#         #     print(123,form_teacher.instance.t_no)
#         #     teacher_info = teacher_tbl.objects.get(t_name = form_teacher.instance.t_no)
#         #     form = LectureForm()
#         #     form_teacher = LectureForm_teacher(request.POST)
#         #     print(teacher_info.t_no)
#         #     context = {'teacher_info' : teacher_info, 'form': form, 'form_teacher' : form_teacher}
#         #
#         #     return render(request, 'admin/lecture_form.html', context)
#
#         # if form.is_valid():
#         #     # print(333,teacher_info.t_no)
#         #     lecture_tbl = form.save(commit=False)
#         #     # lecture_tbl.t_no = teacher_info.t_no
#         #     lecture_tbl.l_img = request.FILES['l_img']
#         #     lecture_tbl.save()
#
#             # return redirect('admin:index')
#
#     else:
#         form = LectureForm()
#         # form_teacher = LectureForm_teacher()
#
#     teacher_list = teacher_tbl.objects.order_by('-t_join')
#     context = {'form' : form, 'teacher_list' : teacher_list}
#
#     return render(request, 'admin/lecture_form.html', context)
# 강의 등록

def lecture_create(request):
    """
    lecture 등록
    """
    if request.method == 'POST':
        form_teacher = LectureForm_teacher(request.POST)
        form = LectureForm()

        if request.POST['버튼'] == '1':
            print(request.POST)
            teacher_info = teacher_tbl.objects.get(pk=request.POST['t_no'])
            form_teacher = LectureForm_teacher(request.POST)
            teacher_t_no = request.POST['t_no']
            context = { 'teacher_info' : teacher_info, 'form_teacher' : form_teacher, 'form' :form, 'teacher_t_no' : teacher_t_no }

            return render(request, 'admin/lecture_form.html', context)

        if request.POST['버튼'] == '2':
            form = LectureForm(request.POST)
            print(request.POST)
            lecture_tbl = form.save(commit=False)
            lecture_tbl.t_no_id = request.POST['gg']
            lecture_tbl.l_img = request.FILES['l_img']

            # lecture_tbl.l_totalnum = request.POST['l_totalnum']
            # lecture_tbl.l_term = request.POST['l_term']
            # lecture_tbl.l_pay = request.POST['l_pay']
            # lecture_tbl.l_startdate= request.POST['l_startdate']
            # lecture_tbl.l_desc = request.POST['l_desc']
            # lecture_tbl.l_dept = request.POST['l_dept']
            # lecture_tbl.l_class = request.POST['l_class']
            # lecture_tbl.l_subject = request.POST['l_subject']
            lecture_tbl.save()

            return redirect('admin:index')
            # lecture_tbl.l_totalnum = 40
            # lecture_tbl.t_no_id = int(request.POST['gg'])
            # lecture_tbl.l_img = request.FILES['l_img']
            # lecture_tbl.save()
                # if form.is_valid():
                # lecture_tbl = form.save(commit=False)
                # lecture_tbl.t_no = request.POST
                # lecture_tbl.l_img = request.FILES['l_img']
                # lecture_tbl.l_img.save()
                # print(request.POST)


        # print(222,request.FILES['l_img'])
        # form_teacher = LectureForm_teacher()
        # form = LectureForm()
        # print(form.clean())
        # if form_teacher.is_valid():
        #
        #     print(123,form_teacher.instance.t_no)
        #     teacher_info = teacher_tbl.objects.get(t_name = form_teacher.instance.t_no)
        #     form = LectureForm()
        #     form_teacher = LectureForm_teacher(request.POST)
        #     print(teacher_info.t_no)
        #     context = {'teacher_info' : teacher_info, 'form': form, 'form_teacher' : form_teacher}
        #
        #     return render(request, 'admin/lecture_form.html', context)

        # if form.is_valid():
        #     # print(333,teacher_info.t_no)
        #     lecture_tbl = form.save(commit=False)
        #     # lecture_tbl.t_no = teacher_info.t_no
        #     lecture_tbl.l_img = request.FILES['l_img']
        #     lecture_tbl.save()

            # return redirect('admin:index')

    else:
        form = LectureForm()
        form_teacher = LectureForm_teacher()

    teacher_list = teacher_tbl.objects.order_by('-t_join')
    context = {'form' : form, 'teacher_list' : teacher_list, 'form_teacher' : form_teacher}

    return render(request, 'admin/lecture_form.html', context)

# 학부모 목록
def parents_list(request):
    customer_list = customer_tbl.objects.order_by('-c_join')
    # customer_tbl.objects.get(pk = )

    context = {'customer_list': customer_list}


    return render(request, 'admin/parent_list.html', context)

# 로그인
def login_admin(request):
    if request.method == "POST":
        # print(request)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password=password)
        if user is not None:
            print("인증 성공")
            login(request, user)

            return redirect('/admin')

        else:
            print("인증 실패")

    return render(request, 'admin/login.html')

def logout_admin(request):
    logout(request)

    return redirect('/admin')

def consult_list(request):
    return render(request, 'admin/consult_list.html')

# 병훈 --------------------------------------------------------------

#공지 등록하기
def notice(request):
    """
    notice 등록
    """
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice_tbl = form.save(commit=False)
            notice_tbl.n_writer = "관리자"
            notice_tbl.notice_date = timezone.now()
            notice_tbl.save()

            return redirect('admin:index')
    else:
        form = NoticeForm()
    context = {'form': form}
    return render(request, 'admin/notice.html', context)


#공지 목록 보기
def noticelist(request):
    notice_list = notice_tbl.objects.order_by
    context = {'notice_list':notice_list}
    return render(request,'admin/noticelist.html',context)

#자주하는 질문 등록하기
def faq(request):
    """
    Faq 등록
    """
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            faq_tbl = form.save(commit=False)
            faq_tbl.faq_date = timezone.now()
            faq_tbl.save()

            return redirect('admin:index')
    else:
        form = FaqForm()
    context = {'form': form}
    return render(request,'admin/faq.html',context)
#자주하는 질문 리스트

def faqlist(request):
    faq_list = faq_tbl.objects.order_by
    # faq_list_detail = []
    context = {'faq_list': faq_list}
    return render(request, 'admin/faqlist.html', context)

#공지상세
def noticedetail(request, notice_tbl_t_no):
    """
    detail 내용 출력
    """
    detail = notice_tbl.objects.get(pk = notice_tbl_t_no)
    context = {'detail':detail}
    return render(request,'admin/noticedetail.html',context)

#공지 수정
def detail_modify(request, notice_tbl_t_no):
    """
    detail 내용 수정
    """
    detail = notice_tbl.objects.get(pk = notice_tbl_t_no)

    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            notice_tbl = form.save(commit=False)
            notice_tbl.notice_date = timezone.now()
            notice_tbl.save()
            return redirect('admin:index')
    else:
        form = NoticeForm(instance=notice)
    context = {'form': form}
    return render(request, 'admin/noticedetail.html', context)

#공지 삭제

def detail_delete(request, notice_tbl_t_no):
    """
    detail 질문삭제
    """
    detail = notice_tbl.objects.get(pk=notice_tbl_t_no)
    detail.delete()
    return redirect('admin/index')

# # 자주하는 질문 상세보기
# def faqlist_detail(request, faq_no):
#     faq_list = faq_tbl.objects.order_by
#     faq_list_detail = faq_list.objects.get(pk = faq_no)
#     context = {'faq_list': faq_list, 'faq_list_detail' : faq_list_detail}
#     return render(request, 'admin/faqlist.html', context)




