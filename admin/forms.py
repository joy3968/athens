from django import forms
from admin.models import *


class LectureForm(forms.ModelForm):
    class Meta:
        model = lecture_tbl
        fields = ['l_totalnum', 'l_term', 'l_pay', 'l_startdate', 'l_desc', 'l_dept', 'l_class', 'l_subject']

        widgets = {
            # 't_no': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'l_totalnum': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
            'l_term': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'l_pay': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'l_startdate': forms.DateInput(attrs={'class': 'form-control date-picker' ,'rows': 5}),
            # 'l_img' : forms.ClearableFileInput(attrs={'class': 'form-control', 'rows': 5}),
            'l_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'l_dept': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'l_class': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'l_subject': forms.Select(attrs={'class': 'form-control', 'rows': 5}),

        }

        labels = {
            # 't_no': '선생님 성함',
            'l_totalnum': '학생 정원',
            'l_term': '강의 기간',
            'l_pay': '강의료(1개월 기준)',
            'l_startdate': '강의 시작일',
            'l_desc': '강의 설명',
            # 'l_img' : '커리큘럼 이미지',
            'l_dept': '부서(중등부/고등부)',
            'l_class': '학년',
            'l_subject': '과목',
        }

class LectureForm_teacher(forms.ModelForm):
    class Meta:
        model = lecture_tbl

        fields = ['t_no']

        widgets = {
            't_no': forms.Select(attrs={'class': 'form-control', 'row' : 5})}

        labels = {
            't_no': '선생님 성함'}

# class userpage_form(forms.ModelForm):
#     class Meta:
#         model = userpage_tbl
#
#         fields = ['page_img_main', 'page_img_sub1', 'page_img_sub2']
#
#         widgets = {
#             'page_img_main': forms.ImageField(attrs={'class': 'form-control', 'row' : 5})}
#
#         labels = {
#             't_no': '선생님 성함'}




# 병훈 --------------------------------------------------------------

class NoticeForm(forms.ModelForm):
    class Meta:
        model = notice_tbl
        fields = ['notice_no','notice_target','notice_title','notice_content']

        widgets = {
            'notice_target': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'notice_title': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
            'notice_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

        labels = {
            'notice_title':'공지글 제목',
            'notice_date':'공지 날짜',
            'notice_target':'공지 대상',
            'notice_content':'내용'
        }

class FaqForm(forms.ModelForm):
    class Meta:
        model = faq_tbl
        fields = ['faq_no','faq_question','faq_answer',]

        widgets = {
            'faq_question': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'faq_answer': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

        labels = {
            'faq_question':'질문 내용',
            'faq_answer':'질문 답변',
        }



