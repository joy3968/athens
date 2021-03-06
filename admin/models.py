from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class customer_tbl(models.Model):
    c_no = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=10)
    c_id = models.CharField(max_length=40, unique=True)
    c_pw = models.CharField(max_length=100)
    c_phone = models.CharField(max_length=20)
    c_gender = models.CharField(max_length=10)
    c_join = models.DateField(auto_now_add=True)
    c_birth = models.DateField()
    c_code = models.CharField(max_length=6, null=True)
    c_add = models.CharField(max_length=50, null=True)
    c_school = models.CharField(max_length=50, null=True)
    c_state = models.BooleanField()
    # 수정
    c_out = models.DateField(null=True)
    # 학부모 일 경우 자식의 학생 코드
    c_code_valid = models.CharField(max_length=6, null=True)


class teacher_tbl(models.Model):
    t_no = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=10)
    t_id = models.CharField(max_length=40, unique=True)
    t_pw = models.CharField(max_length=100)
    t_phone = models.CharField(max_length=20, null=True)
    t_gender = models.CharField(max_length=10)
    t_birth = models.DateField()
    t_state = models.BooleanField()
    t_add = models.CharField(max_length=50, null=True)
    t_join = models.DateField(auto_now_add=True)
    t_file = models.ImageField(upload_to='teacher/', blank=True)
    t_out = models.DateField(null=True)
    t_text = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.t_name

class lecture_tbl(models.Model):
    l_no = models.AutoField(primary_key=True)
    l_totalnum = models.IntegerField()
    # 강의 기간 선택

    term_choice = ((1,'1개월'),(2,'2개월'),(3,'3개월'))
    l_term = models.IntegerField(choices = term_choice)

    # 강의료 선택
    pay_choice = ((280000, '중등 : 280,000원'),(350000, '고등 : 350,000원'))
    l_pay = models.IntegerField(choices = pay_choice)

    l_startdate = models.DateField()

    # 부서 Choice
    t_no = models.ForeignKey(teacher_tbl , on_delete=models.CASCADE)
    l_desc = models.CharField(max_length=200, null=True)
    l_img = models.ImageField(upload_to='lecture/%Y/%m/%d', null=True)

    # 부서 Choice
    dept_choice = (('중등' , '중등'), ('고등', '고등'))

    l_dept = models.CharField(max_length=20, choices = dept_choice)

    # 학년 Choice
    class_choice = (('1', '1학년'), ('2' ,'2학년'), ('3' ,'3학년'))
    l_class = models.CharField(max_length=10, choices = class_choice)
    # 선택 Choice
    subject_choice = (('수학','수학'), ('영어', '영어'))
    l_subject = models.CharField(max_length=10, choices = subject_choice)

class training_tbl(models.Model):
    tr_no = models.AutoField(primary_key=True)
    tr_date = models.DateField(auto_now_add=True)
    l_no = models.ForeignKey(lecture_tbl, on_delete=models.CASCADE)
    c_no = models.ForeignKey(customer_tbl, on_delete=models.CASCADE)

# 자주하는 질문
class faq_tbl(models.Model):
    faq_no = models.AutoField(primary_key=True)
    faq_question = models.TextField()
    faq_answer = models.TextField()
    faq_date = models.DateTimeField()

# 공지사항
class notice_tbl(models.Model):
    notice_no = models.AutoField(primary_key=True)
    notice_title = models.CharField(max_length=200)
    n_writer = models.CharField(max_length=20)
    notice_date = models.DateTimeField()
    subject_choice = (('선생님', '선생님'), ('전체', '전체'))
    notice_target = models.CharField(max_length=20, choices=subject_choice)
    notice_content = models.TextField()



# 온라인자료 - 파일 컬럼 추가
class online_tbl(models.Model):
    on_no = models.AutoField(primary_key=True)
    on_title = models.CharField(max_length=200)
    l_no = models.ForeignKey(lecture_tbl, on_delete=models.CASCADE)
    on_content = models.TextField()
    on_date = models.DateTimeField()
    on_div = models.CharField(max_length=20)
    # ON_FILE = models.FileField(upload_to=,blank=True)

# # 문의게시판
# class qna_tbl(models.Model):
#     qna_no = models.AutoField(primary_key=True)
#     qna_title = models.CharField(max_length=200)
#     qna_content = models.TextField()
#     qna_date = models.DateTimeField()
#     c_no = models.ForeignKey(customer_tbl, on_delete=models.CASCADE)
#     qna_state = models.CharField(max_length=20)
#
# # 문의답글
# class reply_tbl(models.Model):
#     re_no = models.AutoField(primary_key=True)
#     re_writer = models.CharField(max_length=20)
#     re_date = models.DateTimeField()
#     re_content = models.TextField()

# 출결
class attendance_tbl(models.Model):
    at_no = models.AutoField(primary_key=True)
    attendance = models.CharField(max_length=20)
    tr_no = models.ForeignKey(training_tbl, on_delete=models.CASCADE)
    at_date = models.DateField()

# 시험
class test_tbl(models.Model):
    te_no = models.AutoField(primary_key=True)
    te_name = models.CharField(max_length=200)
    te_score = models.IntegerField(null=True,blank=True)
    te_date = models.DateField()
    tr_no = models.ForeignKey(training_tbl, on_delete=models.CASCADE)

# 상담
class consult_tbl(models.Model):
    cu_no = models.AutoField(primary_key=True)
    cu_cust = models.CharField(max_length=20)
    cu_join_time = models.DateTimeField()
    cu_res_time = models.DateTimeField()
    cu_content = models.TextField(null=True,blank=True)
    cu_state = models.CharField(max_length=10, null=True, blank=True)
    c_no = models.ForeignKey(customer_tbl, on_delete=models.CASCADE)
    t_no = models.ForeignKey(training_tbl, on_delete=models.CASCADE)

class userpage_tbl(models.Model):
    page_img_main = models.ImageField(upload_to='userpage/', null=True, blank=True)
    page_img_sub1 = models.ImageField(upload_to='userpage/', null=True, blank=True)
    page_img_sub2 = models.ImageField(upload_to='userpage/', null=True, blank=True)

# class cust_info(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE) # 현 계정의 사용자를 가져올 수 있음.
#     c_no = models.AutoField(primary_key=True)
#     c_name = models.CharField(max_length=10)
#     c_id = models.CharField(max_length=40, unique=True)
#     c_pw = models.CharField(max_length=100)
#     c_phone = models.CharField(max_length=20)
#     c_gender = models.CharField(max_length=10)
#     c_join = models.DateField(auto_now_add=True)
#     c_birth = models.DateField()
#     c_code = models.CharField(max_length=6, null=True)
#     c_add = models.CharField(max_length=50, null=True)
#     c_school = models.CharField(max_length=50, null=True)
#     c_state = models.BooleanField()
#     # 수정
#     c_out = models.DateField(null=True)
#     # 학부모 일 경우 자식의 학생 코드
#     c_code_valid = models.CharField(max_length=6, null=True)

# class teacher_info(models.Model):
#     user = models.OneToOneField(customer_tbl.AUTH_USER_MODEL) # 현 계정의 사용자를 가져올 수 있음.
#     nickname = models.CharField(max_length=64)
#     profile_photo = models.ImageField(blank=True)

