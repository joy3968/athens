from admin.models import *
from django.utils import timezone
from django.shortcuts import render, redirect
import requests

# Create your views here.

from django.http import HttpResponse


# 수강신청(결제)
def order(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            # for item in cart:
            lecture_instance = lecture_tbl.objects.get(pk=1)
            OrderItem.objects.create(order=order, price=2000,
                                         quantity=1)
            lecture_list = lecture_tbl.objects.order_by
            context = {'lecture_list': lecture_list, 'order' : order}
            # cart.clear()
            return render(request, 'order/order.html', context)

    else:
        lecture_list = lecture_tbl.objects.order_by
        form = OrderCreateForm(request.POST)
        context = {'lecture_list': lecture_list, 'form': form}
    return render(request, 'order/order.html', context)

    # if request.method == 'POST':
    #     print(request.POST)
    #     l_no = request.POST['l_no']
    #     print(request.POST['l_no'])
    #     # c_no_id 는 user의 id를통해 고객의 c_no를 뽑아와야함.
    #     tr_instance = training_tbl(tr_date=timezone.now(), c_no_id=1, l_no_id=l_no)
    #     # 수강 테이블의 새로운 객체 생성
    #     tr_instance.save()
    #
    #
    # lecture_list = lecture_tbl.objects.order_by
    # context = {'lecture_list' : lecture_list}
    # return render(request, 'order/order.html', context)

# # 카카오페이 결제
# def kakao(request):
#     if request.method == "POST":
#         URL = 'https://kapi.kakao.com/v1/payment/ready'
#         headers = {
#             "Authorization": "KakaoAK " + "Kakao Developers에서 생성한 앱의 어드민 키",  # 변경불가
#             "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
#         }
#         params = {
#             "cid": "TC0ONETIME",  # 테스트용 코드
#             "partner_order_id": "1001",  # 주문번호
#             "partner_user_id": "german",  # 유저 아이디
#             "item_name": "연어초밥",  # 구매 물품 이름
#             "quantity": "1",  # 구매 물품 수량
#             "total_amount": "12000",  # 구매 물품 가격
#             "tax_free_amount": "0",  # 구매 물품 비과세
#             "approval_url": "결제 성공 시 이동할 url",
#             "cancel_url": "결제 취소 시 이동할 url",
#             "fail_url": "결제 실패 시 이동할 url",
#         }
#
#         res = requests.post(URL, headers=headers, params=params)
#         request.session['tid'] = res.json()['tid']  # 결제 승인시 사용할 tid를 세션에 저장
#         next_url = res.json()['next_redirect_pc_url']  # 결제 페이지로 넘어갈 url을 저장
#         return redirect(next_url)
#
#     return render(request, 'order/kakao.html')


# #############################################
# from django.views.generic.base import View
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import *
#
#
#
# class PointCheckoutAjaxView(View):
#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated():
#             return JsonResponse({}, status=401)
#
#         user = request.user
#         amount = request.POST.get('amount')
#         type = request.POST.get('type')
#
#         try:
#             trans = PointTransaction.objects.create_new(
#                 user=user,
#                 amount=amount,
#                 type=type
#             )
#         except:
#             trans = None
#
#         if trans is not None:
#             data = {
#                 "works": True,
#                 "merchant_id": trans
#             }
#             return JsonResponse(data)
#         else:
#             return JsonResponse({}, status=401)
#
#
# class PointImpAjaxView(View):
#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated():
#             return JsonResponse({}, status=401)
#
#         user = request.user
#         merchant_id = request.POST.get('merchant_id')
#         imp_id = request.POST.get('imp_id')
#         amount = request.POST.get('amount')
#
#         try:
#             trans = PointTransaction.objects.get(
#                 user=user,
#                 order_id=merchant_id,
#                 amount=amount
#             )
#         except:
#             trans = None
#
#         if trans is not None:
#             trans.transaction_id = imp_id
#             trans.success = True
#             trans.save()
#
#             data = {
#                 "works": True
#             }
#
#             return JsonResponse(data)
#         else:
#             return JsonResponse({}, status=401)
#
# def charge_point(request):
#     template = 'order/charge.html'
#
#     return render(request, 'order/charge.html')


#####################################################
from django.shortcuts import render, get_object_or_404
from admin.models import *
# from cart.cart import Cart
from .models import *
from .forms import *

# def order_create(request):
#     if request.method == 'POST':
#         # print(request.POST)
#         l_no = request.POST['l_no']
#         # print(request.POST['l_no'])
#         # c_no_id 는 user의 id를통해 고객의 c_no를 뽑아와야함.
#         tr_instance = training_tbl(tr_date=timezone.now(), c_no_id=1, l_no_id=l_no)
#         # 수강 테이블의 새로운 객체 생성
#         tr_instance.save()
#
#
#     lecture_list = lecture_tbl.objects.order_by
#     context = {'lecture_list' : lecture_list}

def order_create(request):
    # cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            # for item in cart:
            lecture_instance = lecture_tbl.objects.get(pk=1)
            OrderItem.objects.create(order=order, price=2000,
                                         quantity=1)

            # cart.clear()
            return render(request, 'order/create.html', {'order':order})

    else:
        form = OrderCreateForm(request.POST)
    return render(request, 'order/create.html', {'form':form})

# ajax로 결제 후에 보여줄 결제 완료 화면

def order_complete(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id=order_id)
    return render(request,'order/created.html',{'order':order})

# 결제를 위한 임포트
from django.views.generic.base import View
from django.http import JsonResponse

class OrderCreateAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated":False}, status=403)

        # # cart = Cart(request)
        # form = OrderCreateForm(request.POST)
        #
        # if form.is_valid():
        #     order = form.save(commit=False)
        #     order = form.save()
        #     # for item in cart:
        #     OrderItem.objects.create(order=order, price=2000,
        #                              quantity=1)
        #     # cart.clear()
        data = {
            "order_id": 1
        }
        return JsonResponse(data)
        # else:
        #     return JsonResponse({}, status=401)

# 결제 정보 생성
class OrderCheckoutAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated":False}, status=403)

        # order_id = request.POST.get('order_id')
        # order = Order.objects.get(id=order_id)
        # amount = int(request.POST.get('amount'))

        # try:
        #     merchant_order_id = OrderTransaction.objects.create_new(
        #         # order = order,
        #         # amount = amount
        #     )
        # except:
        #     merchant_order_id = None

        # if merchant_order_id is not None:
        data = {
            "works": True,
            # "merchant_id": merchant_order_id
            "merchant_id": 1
        }
        return JsonResponse(data)
        # else:
        #     return JsonResponse({}, status=401)

# 실제 결과가 이뤄진 것이 있는지 확인
class OrderImpAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated":False}, status=403)

        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        merchant_id = request.POST.get('merchant_id')
        imp_id = request.POST.get('imp_id')
        amount = request.POST.get('amount')

        try:
            trans = OrderTransaction.objects.get(
                order=order,
                merchant_order_id=merchant_id,
                amount=amount
            )
        except:
            trans = None

        if trans is not None:
            trans.transaction_id = imp_id
            trans.success = True
            trans.save()
            order.paid = True
            order.save()

            data = {
                "works": True
            }

            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)

# Create your views here.
