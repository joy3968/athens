from django.contrib import admin
from .models import notice_tbl

# 관리자가 게시글 작성
admin.site.register(notice_tbl)
