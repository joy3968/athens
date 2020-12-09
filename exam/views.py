from django.shortcuts import render
import os
from os.path import basename
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import urlquote

from admin.models import *
from django.utils import timezone

## 민우 ----------------------------------------------------------

####################### 선생님 페이지 ##############################

# 시험을 출제할 강의 선택
def lecture_select(request):
    teacher = teacher_tbl.objects.get(user=request.user.id)
    lecture = lecture_tbl.objects.filter(t_no_id=teacher.t_no)

    # 반대로 정렬한다.
    lecture = lecture.reverse()

    context = {'lecture': lecture}

    return render(request, 'exam/lecture_select.html', context)

# 시험 목록
def exam_enroll(request, l_no):
    lecture = lecture_tbl.objects.get(l_no=l_no)
    try:
        # 해당 강의번호와 일치하는 test_list를 불러옵니다.
        test_list = test_tbl.objects.filter(l_no_id=l_no)
    except:
        test_list = None

    # 반대로 정렬한다. (최신 강의를 위쪽에에 나오 하기 위해)
    test_list = test_list.reverse()

    context = {'lecture' : lecture, 'test_list' : test_list}

    return render(request, 'exam/exam_enroll.html', context)


# 시험 등록
def enrollment(request, l_no):

    try:
        lecture_info = lecture_tbl.objects.get(l_no=l_no)
    except:
        pass

    # 등록하기 버튼을 눌렀을 때
    if request.method == 'POST':
        if request.POST['btn'] == '1':
            print(request.POST)
            # 문제 수를 받을 빈 리스트
            number_list = []
            # 문제 수(생성할 문제 수로 입력한 값)
            number = int(request.POST['number'])

            for i in range(number):
                # number_list에 추가
                number_list.append(i+1)

            context = {'lecture_info': lecture_info, 'number_list': number_list}


            return render(request, 'exam/enrollment.html', context)


        if request.POST['btn'] == '2':
            # QueryDict 를 딕셔너리로 변환.
            mydict = dict(request.POST)

            # 입력받은 문제의 수
            number = len(mydict['question_no'])

            # 값을 모두 입력했는지 확인(하나라도 입력하지 않았을 시 모든 값을 입력해 달라는 메세지를 띄운다.)
            for i in range(number):
                # 모두 입력했으면 pass
                if bool(mydict['question'][i]) and bool(mydict['choice_1'][i]) and bool(mydict['choice_2'][i]) and bool(mydict['choice_3'][i]) and bool(mydict['choice_4'][i]) and bool(mydict['answer'][i]):
                    pass
                # 하나라도 입력하지 않았을 시
                else:
                    return HttpResponse('<script type="text/javascript"> alert("모든 값을 입력해 주세요."); history.back();</script>' )

            print(request.POST)
            # test 객체 생성
            test = test_tbl.objects.create(te_name=request.POST['te_name'], l_no_id=l_no)


            # test_detail 객체 생성 (총 5문제 등록)
            for i in range(number):
                # print(request.POST.items())
                test_detail_tbl.objects.create(te_no_id=test.te_no, td_question_no= mydict['question_no'][i] ,td_question=mydict['question'][i],
                                           td_choice_1=mydict['choice_1'][i],td_choice_2=mydict['choice_2'][i],
                                           td_choice_3=mydict['choice_3'][i],td_choice_4=mydict['choice_4'][i],
                                           td_answer=mydict['answer'][i])


            # 등록 완료 후 선생님 메인 페이지로 이동
            return redirect('/teacher')


    # 초기 기본값으로 5문제가 뜨게 한다.
    context={'lecture_info': lecture_info, 'number_list' : [1,2,3,4,5] }

    return render(request, 'exam/enrollment.html', context)

# 시험 수정 페이지
def exam_modify(request, l_no, te_no):
    try:
        lecture_info = lecture_tbl.objects.get(l_no=l_no)
    except:
        pass

    # 초기 기본값으로 5문제가 뜨게 한다.
    context = {'lecture_info': lecture_info, 'number_list': [1, 2, 3, 4, 5]}

    return render(request, 'exam/enrollment.html', context)


####################### 학생/학부모 페이지 ##############################

# 시험 응시하기(학생이 신청한 강의 목록 불러오기) - 사용자(고객) 페이지
def test_lecture_list(request):

    user = request.user
    # 현재 로그인한 학생의 객체를 선택
    try:
        customer_info = customer_tbl.objects.get(user_id=user.id)

        # 학생 코드가 없을 경우(학생이 아닌 경우) -> 학부모인 경우
        if not customer_info.c_code:
            return HttpResponse('<script type="text/javascript"> alert("학생만 시험에 응시하실 수 있습니다."); history.back();</script>' )

    except:
        # customer_tbl의 객체가 아닌 경우 (학생or학부모가) 아닌 경우
        return HttpResponse('<script type="text/javascript"> alert("학생만 시험에 응시하실 수 있습니다."); history.back();</script>' )

    # 그 학생이 수강하고 있는 강의리스트를 filter를 통해 가져온다.
    training_list = training_tbl.objects.filter(c_no_id=customer_info.c_no)

    context = {'training_list': training_list}


    if request.method == 'POST':
        print(request.POST)
        # 응시할 시험을 선택하고 다음을 눌렀을 경우.
        if request.POST['btn'] == 'lecture':
            print(request.POST)

            # @를 기준으로 자른다(l_no와 tr_no 분리하기 위해)
            split_list = request.POST['l_no'].split('@')
            # 앞에 저장된 값은 l_no
            l_no = split_list[0]
            # 뒤에 저장된 값은 tr_no
            tr_no = split_list[1]

            # 해당 강의의 시험 리스트를 filter를 통해 불러온다.
            test_list = test_tbl.objects.filter(l_no_id = l_no)

            ### 만약 해당 학생이 그 시험을 봤다면 리스트에 나오지 않기 위해 걸러준다. ###

            # 이미 응시한 시험을 거르기 위한 빈 리스트(응시하지 않은 시험 객체만 담기 위함)
            test_list_filter = []

            for test in test_list:
                print(test.te_no)
                try:
                    # 시험 응시 테이블에 걸리는지 확인(해당 시험에 대해 응시했는지 확인 - 에러가 난다면 응시하지 않은것)
                    test_apply.objects.get(te_no_id=test.te_no, tr_no_id=tr_no)
                except:
                    # 응시하지 않았을 시에 test_list_filter 리스트에 넣는다.(시험을 응시하지 않은 것만)
                    test_list_filter.append(test)

            context = {'test_list' : test_list_filter, 'tr_no': tr_no}

            return render(request, 'exam/student_test_select.html', context)

        # 시험을 선택하고 다음을 눌렀을 경우.
        elif request.POST['btn'] == 'test':
            print(request.POST)
            print(request.POST['te_no'])

            te_no = request.POST['te_no']
            # 해당 시험의 문제 리스트를 모두 불러옵니다.
            test_detail_list = test_detail_tbl.objects.filter(te_no_id=te_no)
            tr_no = request.POST['tr_no']

            context = {'test_detail_list' : test_detail_list, 'tr_no' : tr_no}


            return render(request, 'exam/test_start.html', context)

            # return render(request,)

        elif request.POST['btn'] == 'test_submit':


            # 해당 시험을 불러 옵니다.
            te_no = request.POST['te_no']
            # 해당 학생의 수강 번호를 불러 옵니다.
            tr_no = request.POST['tr_no']

            test = test_tbl.objects.get(pk=te_no)

            # 시험 상세 리스트를 불러옵니다.(문제와 정답이 있는 테이블)
            test_detail_list = test_detail_tbl.objects.filter(te_no_id=te_no)

            # QueryDict 를 딕셔너리로 변환.
            mydict = dict(request.POST)

            # 해당 학생의 정답 제출 리스트
            student_answer = mydict['answer']

            # 문제의 갯수
            number = len(student_answer)

            # 맞은 갯수를 체크하기 위한 초기값.
            count = 0

            for i in range(len(test_detail_list)):
                # print(test.td_question)

                # 해당 문제의 정답
                answer = test_detail_list[i].td_answer

                if int(student_answer[i]) == int(answer):
                    # 맞았을 경우 20점 추가 (총 5문제 이므로)
                    count += 1
                else:
                    print('틀렸습니다.')


            #점수를 매긴다. 소수자리는 반올림을 한다.
            score = round((count / number)*100)

            # 이미 해당 시험을 봤으면 걸러내기. (시험을 다 본 후 뒤로가기 해서 다시 제출했을 경우 방지)
            try:
                # 해당 시험을 제출했을 경우 메세지를 띄운다.
                test_apply.objects.get(te_no_id=te_no, tr_no_id=tr_no)
                return HttpResponse('<script type="text/javascript"> alert("이미 해당 시험에 응시하셨습니다."); history.back();</script>')
            except:
                # 그렇지 않을 경우(시험에 보지 않았을 경우) 다음 단계 진행.
                pass

            # test_apply 테이블에 시험 점수 등록( test_apply 테이블에 저장 )
            test_apply.objects.create(te_score=score, te_no_id=te_no, tr_no_id=tr_no)

            # 시험 점수를 보여주기 위해 context에 score저장
            context = {'score' : score}
            return render(request, 'exam/test_result.html', context)


    return render(request, 'exam/student_lecture_select.html', context)

# Create your views here.
