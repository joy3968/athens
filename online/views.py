import os
from os.path import basename
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import urlquote

from admin.models import *
from django.utils import timezone


def select_lecture_teacher(request):
    teacher = teacher_tbl.objects.get(user=request.user.id)
    lecture =lecture_tbl.objects.filter(t_no_id=teacher.t_no)
    context = {'lecture':lecture}
    return render(request, 'online/select_lecture.html', context)

def select_online_index_teacher(request,pk):

    lecture = lecture_tbl.objects.get(l_no=pk)
    online= online_tbl.objects.filter(l_no_id=lecture.l_no).order_by('-on_date')
    # 페이징
    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(online, 10)  # 페이지당 10개
    page_obj = paginator.get_page(page)
    context = {'online': page_obj}

    return render(request, 'online/select_online_teacher.html', context)

def post_online(request):
    teacher = teacher_tbl.objects.get(user=request.user.id)
    lecture = lecture_tbl.objects.filter(t_no_id=teacher.t_no)
    context={'lecture':lecture}
    if request.method == "POST":
        select_lec = lecture_tbl.objects.get(l_name=request.POST['l_name'])
        print(request.POST)
        post=online_tbl.objects.create(on_title=request.POST['on_title'],on_content=request.POST['on_content'],on_div=request.POST['on_div'],l_no_id=select_lec.l_no,on_date=timezone.now())
        try:
            if request.FILES['on_file']:
                post.on_file = request.FILES['on_file']
        except:
            pass
        post.save()
        return redirect('/teacher/online/%s'%(select_lec.l_no))

    else:
        return render(request, 'online/online_post.html', context)

def online_contents(request,pk):
    content = online_tbl.objects.get(pk=pk)
    fname=''
    fsize=0
    if content.on_file:
        file = content.on_file
        fname= basename(file.name)
        try:
            with open('%s'%(fname),'wb') as fp:
                for chunk in file.chunks():
                    fp.write(chunk)
            fsize=round(os.path.getsize(fname)/1024)
        except:
            pass
    context={'content':content,'fname':fname,'fsize':fsize}
    return render(request, 'online/online_contents_t.html', context)

def online_download(request):
    id=request.GET['on_no']
    file = online_tbl.objects.get(on_no=id)
    path= file.on_file.name
    filename = basename(path)
    filename=urlquote(filename)
    with open(path,'rb') as download:
        response=HttpResponse(download.read(),content_type='application/octet-stream')
        response['Content-Disposition']=\
            "attchment;filename*=UTF-8''{0}".format(filename)
        return response

def online_update(request):
    teacher = teacher_tbl.objects.get(user=request.user.id)
    lecture = lecture_tbl.objects.filter(t_no_id=teacher.t_no)
    id=request.GET['on_no']
    update = online_tbl.objects.get(on_no=id)

    if request.method == 'POST':
        print('save')
        select_lec = lecture_tbl.objects.get(l_name=request.POST['l_name'])
        update.on_title = request.POST['on_title']
        try:
            if request.FILES['on_file']:
                file = request.FILES['on_file']
                update.on_file = file
        except:
            pass
        update.on_div = request.POST['on_div']
        update.on_content = request.POST['on_content']
        update.l_no_id = select_lec.l_no
        update.save()
        return redirect('/teacher/online/content/%s'%(update.on_no))
    else:
        context = {'update': update, 'lecture': lecture}
        return render(request,'online/online_contents_update.html',context)

def online_delete(request):
    id=request.POST['on_no']
    lecture = online_tbl.objects.get(on_no=id)
    online_tbl.objects.get(on_no=id).delete()
    return redirect('/teacher/online/%s'%(lecture.l_no.l_no))