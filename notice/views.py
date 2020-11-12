from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from admin.models import *

# Create your views here.

# notice_index.html을 부르는 notice_index 함수

def notice_index(request):
    # 공지사항 목록 불러오기
    noticelist = notice_tbl.objects.order_by('-notice_date')

    # 페이징
    page = request.GET.get('page','1') # 페이지
    paginator = Paginator(noticelist,5) # 페이지당 5개
    page_obj = paginator.get_page(page)
    context = {'noticelist':page_obj}

    # notice_list.html을 열 때 , 모든 notice인 noticelist도 가져옵니다.
    return render(request, 'notice/notice_index.html',context)

# notice_content.html을 부르는 notice_content 함수
def notice_content(request,pk):
    # 공지사항 pk이용해서 찾기
    content = notice_tbl.objects.get(pk=pk)
    # notice_content.html을 열 때, 찾은 게시글을 content로 받는다.
    return render(request,'notice/notice_content.html',{'content':content})
