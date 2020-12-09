from django.urls import path

from . import views

app_nap = 'find'

urlpatterns = [

    path('', views.C_find),
    path('T', views.T_find),
    path('pw_find', views.pw_find),
    path('pw_find/reset/', views.auth_pw_reset_view, name='recovery_pw_reset'),

]