from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name='notice'

urlpatterns = [
    path('',notice_index),
    path('notice/<int:pk>', notice_content, name = 'notice_content'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)