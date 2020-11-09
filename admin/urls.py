from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('teacher.in', views.teacher_in, name='teacherin'),
    path('teacher.out', views.teacher_out, name='teacherout'),
    path('teacher_detail/<int:teacher_tbl_t_no>', views.teacher_detail, name='teacher_detail'),
    path('student.in', views.student_in, name='studentin'),
    path('student.out', views.student_out, name='studentout'),
    path('student_detail', views.student_detail, name='student_detail'),
    path('lecture', views.lecture_create, name='lecture_create'),
    path('parents_list', views.parents_list, name='parents_list'),

]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)