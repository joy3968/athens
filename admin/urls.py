from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'admin'

urlpatterns = [
    # ------------------------------ 민우
    path('', views.index, name='index'),
    path('teacher.in', views.teacher_in, name='teacherin'),
    path('teacher.out', views.teacher_out, name='teacherout'),
    path('teacher_detail/<int:teacher_tbl_t_no>', views.teacher_detail, name='teacher_detail'),
    path('student.in', views.student_in, name='studentin'),
    path('student.out', views.student_out, name='studentout'),
    path('student_detail/<int:c_no>', views.student_detail, name='student_detail'),
    path('lecture', views.lecture_create, name='lecture_create'),
    path('parents_list', views.parents_list, name='parents_list'),
    path('login', views.login_admin, name='login_admin'),
    path('logout', views.logout_admin, name='logout_admin'),
    path('consult_list', views.consult_list, name='consult_list'),
    path('userpage', views.userpage, name='userpage'),
    #-----------------------------------------------------병훈
    path('notice', views.notice, name='notice'),
    path('faq', views.faq, name='faq'),
    path('noticelist', views.noticelist, name='noticelist'),
    # path('test', views.test, name='test'),
    # path('testtest', views.testtest, name='testtest'),
    path('noticedetail/<int:notice_tbl_t_no>', views.noticedetail, name='noticedetail'),
    # path('noticedetail/modify/<int:notice_tbl_t_no/',views.detail_modify,name='detail_modify'),
    # path('noticedetail/delete/<int:notice_tbl_t_no>/', views.detail_delete, name='detail_delete'),
    path('faqlist', views.faqlist, name='faqlist'),
    # path('faqlist/<int:faq_no>', views.faqlist_detail, name='faqlist'),


]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)