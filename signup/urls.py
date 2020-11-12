from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name='signup'

urlpatterns = [
  path('sign_up/student/', student_sign_up),
  path('sign_up/parent/', parent_sign_up),
  path('sign_up/teacher/', teacher_sign_up),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)