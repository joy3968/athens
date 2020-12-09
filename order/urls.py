from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'orders'

urlpatterns = [
    path('', views.order, name='order'),
    path('create/', views.order_create, name='order_create'),
    path('create_ajax/', views.OrderCreateAjaxView.as_view(), name='order_create_ajax'),
    path('checkout/', views.OrderCheckoutAjaxView.as_view(), name='order_checkout'),
    path('validation/', views.OrderImpAjaxView.as_view(), name='order_validation'),
    path('complete/', views.order_complete, name='order_complete'),
]