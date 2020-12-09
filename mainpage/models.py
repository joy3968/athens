from django.db import models

class customer_tbl(models.Model):
    c_no = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=10)
    c_id = models.CharField(max_length=40, unique=True)
    c_pw = models.CharField(max_length=18)
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

    class Meta:
        db_table = 'customer'

class teacher_tbl(models.Model):
    t_no = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=10)
    t_id = models.CharField(max_length=40, unique=True)
    t_pw = models.CharField(max_length=18)
    t_phone = models.CharField(max_length=20, null=True)
    t_gender = models.CharField(max_length=10)
    t_birth = models.DateField()
    t_state = models.BooleanField()
    t_add = models.CharField(max_length=50, null=True)
    t_join = models.DateField(auto_now_add=True)
    t_file = models.ImageField(blank=True, upload_to='teacher')
    t_out = models.DateField(null=True)
    t_text = models.CharField(max_length=500, null=True)

class lecture_tbl(models.Model):
    l_no = models.AutoField(primary_key=True)
    l_totalnum = models.IntegerField()
    l_term = models.IntegerField()
    l_pay = models.IntegerField()
    l_startdate = models.DateField()
    t_no = models.ForeignKey(teacher_tbl, on_delete=models.CASCADE)
    l_desc = models.CharField(max_length=200, null=True)
    l_img = models.ImageField(blank=True, upload_to='lecture')
    l_dept = models.CharField(max_length=10)
    l_class = models.IntegerField()
    l_subject = models.CharField(max_length=10)

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
    notice_target = models.CharField(max_length=20)
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

# class cust_info(models.Model):
#     user = models.OneToOneField(customer_tbl.AUTH_USER_MODEL) # 현 계정의 사용자를 가져올 수 있음.
#     nickname = models.CharField(max_length=64)
#
# class teacher_info(models.Model):
#     user = models.OneToOneField(customer_tbl.AUTH_USER_MODEL) # 현 계정의 사용자를 가져올 수 있음.
#     nickname = models.CharField(max_length=64)
#     profile_photo = models.ImageField(blank=True)



# Create your models here.