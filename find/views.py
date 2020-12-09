import json

from django.contrib import messages
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import *
from django.urls import reverse
from .helper import email_auth_num, send_mail


def C_find(request):
    if request.method == 'POST':
        form = C_ID_find(request.POST)
        if form.is_valid():
            c_name = request.POST['c_name']
            c_phone = request.POST['c_phone']
            try:
                # 일치할 때
                c_info = customer_tbl.objects.get(c_name=c_name, c_phone=c_phone)
                return HttpResponse(
                    '<script type="text/javascript">alert("입력된 정보로 가입된 계정은' + c_info.user.username + '입니다."); location.href  ="/login/login"; </script>')
            except:
                # 일치 하는게 없을 때
                return HttpResponse('<script type="text/javascript">alert("가입된 계정이 없습니다."); history.back(); </script>')

    form = C_ID_find()
    context = {'form': form}
    return render(request, 'find/ID_find.html', context)


def T_find(request):
    if request.method == 'POST':
        form = T_ID_find(request.POST)
        if form.is_valid():
            t_name = request.POST['t_name']
            t_phone = request.POST['t_phone']
            try:
                # 일치할 때
                t_info = teacher_tbl.objects.get(t_name=t_name, t_phone=t_phone)
                return HttpResponse(
                    '<script type="text/javascript">alert("입력된 정보로 가입된 계정은' + t_info.user.username + '입니다."); location.href  = "/login/login" ; </script>')
            except:
                # 일치 하는게 없을 때
                return HttpResponse('<script type="text/javascript">alert("가입된 계정이 없습니다."); history.back(); </script>')

    form = T_ID_find()
    context = {'form': form}
    return render(request, 'find/T_ID_find.html', context)


def pw_find(request):
    if request.method == 'POST':
        form = PW_find(request.POST)
        if request.POST['btn'] == '1':
            if request.POST['username']:
                username = request.POST['username']
                try:
                    # 일치할 때
                    info = User.objects.get(username=username)
                    c_info = customer_tbl.objects.get(user_id = info.id)
                    # t_info = teacher_tbl.objects.get(user_id=info.id)

                    auth_num = email_auth_num()

                    c_info.c_auth = auth_num
                    # t_info.t_auth = auth_num

                    c_info.save()
                    # t_info.save()

                    send_mail(
                        '비밀번호 찾기 인증메일입니다.',
                        [username],
                        html=render_to_string('find/recovery_email.html', {
                            'auth_num': auth_num,
                        }),
                    )

                    form = PW_find(request.POST)
                    context = {'a': '1', 'form': form}
                    return render(request, 'find/PW_find.html', context)

                # 일치 하는게 없을 때
                except:
                     return HttpResponse('<script type="text/javascript">alert("가입된 계정이 없습니다."); history.back(); </script>')

        # if request.POST['btn'] == '2':
        #     input_auth_num = request.POST.get('input_auth_num')
        #     if c_info.c_auth == input_auth_num:
        #         target_user = User.objects.get(user_id=user_id, auth=input_auth_num)
        #         target_user.auth = ""
        #         target_user.save()
        #         request.session['auth'] = target_user.user_id
        #         messages.success(request, "인증성공. 새 비밀번호를 설정해 주세요.")
        #         return redirect('pw_find/reset/')
        #     else:
        #         return HttpResponse(
        #             '<script type="text/javascript">alert("인증번호가 틀립니다."); location.href  ="/pw_find"; </script>')

    form = PW_find()
    context = {'form': form}
    return render(request, 'find/PW_find.html', context)



from .forms import Re_PW_set
from login.views import login


def auth_pw_reset_view(request):
    if request.method == 'GET':
        if not request.session.get('auth', False):
            raise PermissionDenied

    if request.method == 'POST':
        session_user = request.session['auth']
        current_user = User.objects.get(username=session_user)
        login(request, current_user)

        reset_password_form = Re_PW_set(request.user, request.POST)

        if reset_password_form.is_valid():
            user = reset_password_form.save()
            messages.success(request, "비밀번호 변경완료! 변경된 비밀번호로 로그인하세요.")
            logout(request)
            return redirect('/login')

        else:
            logout(request)
            request.session['auth'] = session_user
    else:
        reset_password_form = Re_PW_set(request.user)

    return render(request, 'find/password_reset.html', {'form': reset_password_form}),

