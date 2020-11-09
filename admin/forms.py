from django import forms
from admin.models import *

class LectureForm(forms.ModelForm):
    class Meta:
        model = lecture_tbl
        fields = ['t_no', 'l_totalnum', 'l_term', 'l_pay', 'l_startdate', 'l_desc', 'l_dept', 'l_class', 'l_subject']

        widgets = {
            't_no': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'l_totalnum': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
            'l_term': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'l_pay': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'l_startdate': forms.DateInput(attrs={'class': 'form-control', 'rows': 5}),
            # 'l_img' : forms.ClearableFileInput(attrs={'class': 'form-control', 'rows': 5}),
            'l_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'l_dept': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'l_class': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'l_subject': forms.Select(attrs={'class': 'form-control', 'rows': 5}),

        }

        labels = {
            't_no': '선생님 성함',
            'l_totalnum': '학생 정원',
            'l_term' : '강의 기간',
            'l_pay' : '강의료(1개월 기준)',
            'l_startdate' : '강의 시작일',
            'l_desc' : '강의 설명',
            # 'l_img' : '커리큘럼 이미지',
            'l_dept' : '부서(중등부/고등부)',
            'l_class' : '학년',
            'l_subject' : '과목',
        }