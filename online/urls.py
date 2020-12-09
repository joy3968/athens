from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name='online'

urlpatterns = [
    path('teacher/select/lecture/online/',select_lecture_teacher),
    path('teacher/online/<int:pk>',select_online_index_teacher),
    path('teacher/onlinepost/',post_online),
    path('teacher/online/content/<int:pk>',online_contents),
    path('teacher/online/content/download',online_download),
    path('teacher/online/content/update',online_update),
    path('teacher/online/content/delete',online_delete),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)