from django.urls import path
from .views import userlogin,userlogout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


app_name='login'

urlpatterns = [
    path('login/',userlogin),
    path('logout/',userlogout),
]