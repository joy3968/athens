from django.urls import path

from . import views

urlpatterns = [
    path('', views.sign),
    path('S_TOS',views.s_tos),
    path('P_TOS',views.p_tos),
    path('T_TOS',views.t_tos),
]