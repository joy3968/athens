from django.urls import path
from mypage import views

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('pw/', views.mypagepw),
    path('child/',views.mychlid),
    path('add/', views.myaddcode),
]

