from django.urls import path
from .views import *

app_name='consult'

urlpatterns = [
    path('consult/',choose_child),
    path('consult/<int:pk>',choose_teacher),
    path('consult/teacher/<int:pk>',reservation),
    path('consult/teacher/manage/',reservation_manage),
    path('consult/teacher/manage/<int:pk>',reservation_content),
    path('consult/teacher/update/<int:pk>',consult_update),
]