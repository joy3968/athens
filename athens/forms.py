from django import forms
from .models import *

# 학생 회원가입 폼

class studentsignupform(forms.ModelForm):
    re_pw = forms.CharField(label='비밀번호 확인',widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=100)

    class Meta:
        model = customer_tbl
        fields = ['c_name','c_id','c_pw','re_pw','c_phone','c_gender','c_birth','c_add','c_school']
        widgets = {
            'c_name': forms.TextInput(attrs={'class':'form-control'}),
            'c_id': forms.EmailInput(attrs={'class':'form-control'}),
            'c_pw': forms.PasswordInput(attrs={'class':'form-control'}),
            'c_phone': forms.TextInput(attrs={'class':'form-control'}),
            'c_gender': forms.Select(attrs={'class':'form-control'}),
            'c_add': forms.TextInput(attrs={'class':'form-control'}),
            'c_school':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'c_name' : '이름',
            'c_id' : '이메일',
            'c_pw' : '비밀번호(8자 이상)',
            'c_phone' : '전화번호',
            'c_gender' : '성별',
            'c_birth' : '생년월일',
            'c_add' : '주소',
            'c_school' : '학교'
        }
    # 유효성 검사
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('c_id')
        password = cleaned_data.get('c_pw')
        re_password = cleaned_data.get('re_pw')

        # 비밀번호 중복
        if password != re_password:
            self.add_error('c_pw','비밀번호가 다릅니다.')
            self.add_error('re_pw','비밀번호가 다릅니다.')

        # 비밀번호 8자 미만
        if len(password) < 8:
            self.add_error('c_pw','비밀번호는 8자 이상입니다.')

        # 아이디 중복
        try:
            customer_tbl.objects.get(c_id=email)
            self.add_error('c_id','이미 가입된 이메일입니다.')
        except:
            pass

# 학부모 회원가입 폼

class parentsignupform(forms.ModelForm):
    re_pw = forms.CharField(label='비밀번호 확인',widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=100)

    class Meta:
        model = customer_tbl
        fields = ['c_name','c_id','c_pw','re_pw','c_phone','c_gender','c_birth','c_add','c_code_valid']
        widgets = {
            'c_name': forms.TextInput(attrs={'class':'form-control'}),
            'c_id': forms.EmailInput(attrs={'class':'form-control'}),
            'c_pw': forms.PasswordInput(attrs={'class':'form-control'}),
            'c_phone': forms.TextInput(attrs={'class':'form-control'}),
            'c_gender': forms.Select(attrs={'class':'form-control'}),
            'c_add': forms.TextInput(attrs={'class':'form-control'}),
            'c_code_valid': forms.TextInput(attrs={'class':'form-control'})
        }
        labels = {
            'c_name' : '이름',
            'c_id' : '이메일',
            'c_pw' : '비밀번호(8자 이상)',
            'c_phone' : '전화번호',
            'c_gender' : '성별',
            'c_birth' : '생년월일',
            'c_add' : '주소',
            'c_code_valid': '자녀 학생코드(자녀 마이페이지에서 확인가능)'
        }
    # 유효성 검사
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('c_id')
        password = cleaned_data.get('c_pw')
        re_password = cleaned_data.get('re_pw')
        code_valid = cleaned_data.get('c_code_valid')

        # 비밀번호 중복
        if password != re_password:
            self.add_error('c_pw','비밀번호가 다릅니다.')
            self.add_error('re_pw','비밀번호가 다릅니다.')

        # 비밀번호 8자 미만
        if len(password) < 8:
            self.add_error('c_pw','비밀번호는 8자 이상입니다.')

        # 아이디 중복
        try:
            customer_tbl.objects.get(c_id=email)
            self.add_error('c_id','이미 가입된 이메일입니다.')
        except:
            pass

        # 자녀코드 확인
        try:
            customer_tbl.objects.get(c_code=code_valid)
        except:
            self.add_error('c_code_valid', '존재하지 않는 학생 입니다.')


# 선생님 회원가입 폼

class teachersignupform(forms.ModelForm):
    re_pw = forms.CharField(label='비밀번호 확인',widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=100)

    class Meta:
        model = teacher_tbl
        fields = ['t_name','t_id','t_pw','re_pw','t_phone','t_gender','t_birth','t_add','t_file']
        widgets = {
            't_name': forms.TextInput(attrs={'class':'form-control'}),
            't_id': forms.EmailInput(attrs={'class':'form-control'}),
            't_pw': forms.PasswordInput(attrs={'class':'form-control'}),
            't_phone': forms.TextInput(attrs={'class':'form-control'}),
            't_gender': forms.Select(attrs={'class':'form-control'}),
            't_add': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            't_name' : '이름',
            't_id' : '이메일',
            't_pw' : '비밀번호(8자 이상)',
            't_phone' : '전화번호',
            't_gender' : '성별',
            't_birth' : '생년월일',
            't_add' : '주소',
            't_file' : '사진'
        }

    # 유효성 검사
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('t_id')
        password = cleaned_data.get('t_pw')
        re_password = cleaned_data.get('re_pw')

        # 비밀번호 중복
        if password != re_password:
            self.add_error('t_pw','비밀번호가 다릅니다.')
            self.add_error('re_pw','비밀번호가 다릅니다.')

        # 비밀번호 8자 미만
        if len(password) < 8:
            self.add_error('t_pw','비밀번호는 8자 이상입니다.')

        # 아이디 중복
        try:
            customer_tbl.objects.get(t_id=email)
            self.add_error('t_id','이미 가입된 이메일입니다.')
        except:
            pass




