from django.contrib.auth.decorators import *
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from admin.models import *
from .forms import reservationform, timeform
from django.utils import timezone

# Create your views here.

@login_required(login_url='/login/login')
def choose_child(request):
    id = request.user.id
    parents_code = customer_tbl.objects.get(user=id).c_code_valid
    children_list = customer_tbl.objects.filter(c_code=parents_code)
    context = {'children_list': children_list}
    return render(request, 'consult/choose_child.html', context)


# 학부모 -> 학생 -> 수강 -> 강의 -> 선생
@login_required(login_url='/login/login')
def choose_teacher(request, pk):
    try:
        training = training_tbl.objects.filter(c_no=pk)
        teacher_list = []
        for i in range(len(training)):
            teacher_info = training[i].l_no.t_no
            teacher_list.append(teacher_info)

    except:
        pass
    context = {'training': training, 'teacher_list': teacher_list}
    return render(request, 'consult/choose_teacher.html', context)


# 예약
@login_required(login_url='/login/login')
def reservation(request,pk):
    if request.method == "POST":
        if request.POST['button'] == "1":
            timeset = 1
            print(timeset)
            pk_check = pk
            form = reservationform()
            time_form = timeform()
            context = {"form": form, "time_form": time_form, 'timeset': timeset,'pk_check':pk_check}
            return render(request,'consult/reservation.html',context)
        if request.POST['button'] == "2":
            timeset = 2
            print(timeset)
            pk_check = pk
            form = reservationform()
            time_form = timeform()
            context = {"form": form, "time_form": time_form, 'timeset': timeset, 'pk_check':pk_check}
            return render(request, 'consult/reservation.html',context)
        if request.POST['button'] == "3":
            form =reservationform(request.POST)
            time_form = timeform(request.POST)
            if time_form.is_valid():
                customer = customer_tbl.objects.get(user_id=request.user.id)
                teacher = teacher_tbl.objects.get(t_no=pk)
                res_info = consult_tbl.objects.create(c_no_id=customer.c_no,t_no_id=teacher.t_no,cu_res_time=request.POST['cu_res_time'],cu_text=request.POST['cu_text'])
                res_info.cu_join_time = timezone.now()
                res_info.cu_state = '상담대기'
                res_info.save()
                return redirect('/')
            else:
                error = True
                return render(request,'consult/reservation.html',{'error':error})
    else:
        return render(request,'consult/reservation.html')

# 상담 관리
@user_passes_test(lambda u: u.is_staff,login_url='/login')
def reservation_manage(request):
    if request.method =="POST":
        if request.POST['button'] == "1":
            teacher = teacher_tbl.objects.get(user=request.user.id)
            schedule = consult_tbl.objects.filter(t_no_id=teacher.t_no,cu_state="상담대기").order_by('cu_res_time')
            children_list = customer_tbl.objects.all()
            # 페이징
            page = request.GET.get('page', '1')  # 페이지
            paginator = Paginator(schedule, 5)  # 페이지당 5개
            page_obj = paginator.get_page(page)
            context = {'schedule': page_obj, 'children_list': children_list}
            return render(request, 'consult/reservation_manage.html', context)
        elif request.POST['button'] == "2":
            teacher = teacher_tbl.objects.get(user=request.user.id)
            schedule = consult_tbl.objects.filter(t_no_id=teacher.t_no,cu_state="상담완료").order_by('cu_res_time')
            children_list = customer_tbl.objects.all()
            # 페이징
            page = request.GET.get('page', '1')  # 페이지
            paginator = Paginator(schedule, 5)  # 페이지당 5개
            page_obj = paginator.get_page(page)
            context = {'schedule': page_obj, 'children_list': children_list}
            return render(request, 'consult/reservation_manage.html', context)
    else:
        teacher = teacher_tbl.objects.get(user=request.user.id)
        schedule = consult_tbl.objects.filter(t_no_id=teacher.t_no).exclude(cu_state='취소').order_by('cu_res_time')
        children_list = customer_tbl.objects.all()
        # 페이징
        page = request.GET.get('page', '1')  # 페이지
        paginator = Paginator(schedule, 5)  # 페이지당 5개
        page_obj = paginator.get_page(page)
        context = {'schedule': page_obj,'children_list':children_list}
        return render(request,'consult/reservation_manage.html',context)

@user_passes_test(lambda u: u.is_staff,login_url='/login')
def reservation_content(request,pk):

    content = consult_tbl.objects.get(pk=pk)
    children_list = customer_tbl.objects.all()

    if request.method == "POST":
        return redirect('/consult/teacher/update/%s' %(pk))

    context = {'content':content,'children_list':children_list}
    return render(request,'consult/reservation_content.html',context)

@user_passes_test(lambda u: u.is_staff,login_url='/login')
def consult_update(request,pk):

    content = consult_tbl.objects.get(pk=pk)
    children_list = customer_tbl.objects.all()
    context = {'content':content,'children_list':children_list}
    if request.method == "POST":
        content.cu_content= request.POST['cu_content']
        content.cu_state='상담완료'
        content.save()
        return redirect('/consult/teacher/manage/%s' %(pk))
    else:
        return render(request, 'consult/consult_update.html', context)