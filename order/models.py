# # billing/models.py
# from django.db import models
# # User 모델은 알아서 가져오기
# # from .models import User
# from django.db import models
# from .iamport import validation_prepare, get_transaction
# import hashlib
#
#
# # class Point(models.Model):
# #     user = models.OneToOneField(MyUser)
# #     point = models.PositiveIntegerField(default=0)
# #     created = models.DateTimeField(auto_now_add=True, auto_now=False)
# #     timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
# #
# #     def __str__(self):
# #         return str(self.point)
#
#
# class PointTransactionManager(models.Manager):
#     # 새로운 트랜젝션 생성
#     def create_new(self, user, amount, type, success=None, transaction_status=None):
#         if not user:
#             raise ValueError("유저가 확인되지 않습니다.")
#         short_hash = hashlib.sha1(str(random.random())).hexdigest()[:2]
#         time_hash = hashlib.sha1(str(int(time.time()))).hexdigest()[-3:]
#         base = str(user.email).split("@")[0]
#         key = hashlib.sha1(short_hash + time_hash + base).hexdigest()[:10]
#         new_order_id = "%s" % (key)
#
#         # 아임포트 결제 사전 검증 단계
#         validation_prepare(new_order_id, amount)
#
#         # 트랜젝션 저장
#         new_trans = self.model(
#             user=user,
#             order_id=new_order_id,
#             amount=amount,
#             type=type
#         )
#
#         if success is not None:
#             new_trans.success = success
#             new_trans.transaction_status = transaction_status
#
#         new_trans.save(using=self._db)
#         return new_trans.order_id
#
#     # 생선된 트랜잭션 검증
#     def validation_trans(self, merchant_id):
#         result = get_transaction(merchant_id)
#
#         if result['status'] is not 'paid':
#             return result
#         else:
#             return None
#
#     def all_for_user(self, user):
#         return super(PointTransactionManager, self).filter(user=user)
#
#     def get_recent_user(self, user, num):
#         return super(PointTransactionManager, self).filter(user=user)[:num]
#
#
# class PointTransaction(models.Model):
#     user = models.ForeignKey(MyUser)
#     transaction_id = models.CharField(max_length=120, null=True, blank=True)
#     order_id = models.CharField(max_length=120, unique=True)
#     amount = models.PositiveIntegerField(default=0)
#     success = models.BooleanField(default=False)
#     transaction_status = models.CharField(max_length=220, null=True, blank=True)
#     type = models.CharField(max_length=120)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#     objects = PointTransactionManager()
#
#     def __str__(self):
#         return self.order_id
#
#     class Meta:
#         ordering = ['-created']

# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
# from account.models import lecture_tbl
# import hashlib
# from .iamport import payments_prepare, find_transaction
#
# # Create your models here.
#
#
# class Order(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     address = models.CharField(max_length=250)
#     postal_code = models.CharField(max_length=20)
#     city = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['-created']
#
#     def __str__(self):
#         return 'Order {}'.format(self.id)
#
#     def get_total_product(self):
#         return sum(item.get_item_price() for item in self.items.all())
#
#     def get_total_price(self):
#         total_product = self.get_total_product()
#         return total_product - self.discount
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(lecture_tbl, on_delete=models.PROTECT, related_name='order_products')
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return '{}'.format(self.id)
#
#     def get_item_price(self):
#         return self.price * self.quantity
#
#
# class OrderTransactionManager(models.Manager):
#     def create_new(self,order,amount,success=None,transaction_status=None):
#         if not order:
#             raise ValueError("주문 오류")
#
#         order_hash = hashlib.sha1(str(order.id).encode('utf-8')).hexdigest()
#         email_hash = str(order.email).split("@")[0]
#         final_hash = hashlib.sha1((order_hash + email_hash).encode('utf-8')).hexdigest()[:10]
#         merchant_order_id = "%s"%(final_hash)
#
#         payments_prepare(merchant_order_id,amount)
#         tranasction = self.model(
#             order=order,
#             merchant_order_id=merchant_order_id,
#             amount=amount
#         )
#
#         if success is not None:
#             tranasction.success = success
#             tranasction.transaction_status = transaction_status
#
#         try:
#             tranasction.save()
#         except Exception as e:\
#             print("save error", e)
#
#         return tranasction.merchant_order_id
#
#     def get_transaction(self, merchant_order_id):
#         result = find_transaction(merchant_order_id)
#         if result['status'] == 'paid':
#             return result
#         else:
#             return None
#
# class OrderTransaction(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     merchant_order_id = models.CharField(max_length=120, null=True, blank=True)
#     transaction_id = models.CharField(max_length=120, null=True,blank=True)
#     amount = models.PositiveIntegerField(default=0)
#     transaction_status = models.CharField(max_length=220, null=True,blank=True)
#     type = models.CharField(max_length=120,blank=True)
#     created = models.DateTimeField(auto_now_add=True,auto_now=False)
#
#     objects = OrderTransactionManager()
#
#     def __str__(self):
#         return str(self.order.id)
#
#     class Meta:
#         ordering = ['-created']
#
#
# def order_payment_validation(sender, instance, created, *args, **kwargs):
#     if instance.transaction_id:
#         import_transaction = OrderTransaction.objects.get_transaction(merchant_order_id=instance.merchant_order_id)
#
#         merchant_order_id = import_transaction['merchant_order_id']
#         imp_id = import_transaction['imp_id']
#         amount = import_transaction['amount']
#
#         local_transaction = OrderTransaction.objects.filter(merchant_order_id = merchant_order_id,
#                                                             transaction_id = imp_id,amount = amount).exists()
#         if not import_transaction or not local_transaction:
#             raise ValueError("비정상 거래입니다.")
#
# # 결제 정보가 생성된 후에 호출할 함수를 연결해준다.
# from django.db.models.signals import post_save
# post_save.connect(order_payment_validation,sender=OrderTransaction)



#######################################################################


# from django.db import models
# # User 모델은 알아서 가져오기
# from admin.models import User
# from .iamport import validation_prepare, get_transaction
# import hashlib
#
# class Point(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     point = models.PositiveIntegerField(default=0)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return str(self.point)
#
#
# class PointTransactionManager(models.Manager):
#     # 새로운 트랜젝션 생성
#     def create_new(self, user, amount, type, success=None, transaction_status=None):
#         if not user:
#             raise ValueError("유저가 확인되지 않습니다.")
#         short_hash = hashlib.sha1(str(random.random())).hexdigest()[:2]
#         time_hash = hashlib.sha1(str(int(time.time()))).hexdigest()[-3:]
#         base = str(user.email).split("@")[0]
#         key = hashlib.sha1(short_hash + time_hash + base).hexdigest()[:10]
#         new_order_id = "%s" % (key)
#
#         # 아임포트 결제 사전 검증 단계
#         validation_prepare(new_order_id, amount)
#
#         # 트랜젝션 저장
#         new_trans = self.model(
#             user=user,
#             order_id=new_order_id,
#             amount=amount,
#             type=type
#         )
#
#         if success is not None:
#             new_trans.success = success
#             new_trans.transaction_status = transaction_status
#
#         new_trans.save(using=self._db)
#         return new_trans.order_id
#
#     # 생선된 트랜잭션 검증
#     def validation_trans(self, merchant_id):
#         result = get_transaction(merchant_id)
#
#         if result['status'] is not 'paid':
#             return result
#         else:
#             return None
#
#     def all_for_user(self, user):
#         return super(PointTransactionManager, self).filter(user=user)
#
#     def get_recent_user(self, user, num):
#         return super(PointTransactionManager, self).filter(user=user)[:num]
#
#
# class PointTransaction(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     transaction_id = models.CharField(max_length=120, null=True, blank=True)
#     order_id = models.CharField(max_length=120, unique=True)
#     amount = models.PositiveIntegerField(default=0)
#     success = models.BooleanField(default=False)
#     transaction_status = models.CharField(max_length=220, null=True, blank=True)
#     type = models.CharField(max_length=120)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#     objects = PointTransactionManager()
#
#     def __str__(self):
#         return self.order_id
#
#     class Meta:
#         ordering = ['-created']
#
#
# # 트랜잭션이 일어나서 검증하는 post_save
# import time
# import random
# import hashlib
# from django.db.models.signals import post_save
#
# def new_point_trans_validation(sender, instance, created, *args, **kwargs):
#     if instance.transaction_id:
#         # 거래 후 아임포트에서 넘긴 결과
#         v_trans = PointTransaction.objects.validation_trans(
#             merchant_id=instance.order_id
#         )
#
#         res_merchant_id = v_trans['merchant_id']
#         res_imp_id = v_trans['imp_id']
#         res_amount = v_trans['amount']
#
#         # 데이터베이스에 실제 결제된 정보가 있는지 체크
#         r_trans = PointTransaction.objects.filter(
#             order_id=res_merchant_id,
#             transaction_id=res_imp_id,
#             amount=res_amount
#         ).exists()
#
#         if not v_trans or not r_trans:
#             raise ValueError('비정상적인 거래입니다.')
#
#
# post_save.connect(new_point_trans_validation, sender=PointTransaction)


################################################################3
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_product(self):
        return sum(item.get_item_price() for item in self.items.all())

    def get_total_price(self):
        total_product = self.get_total_product()
        return total_product - self.discount

from admin.models import *

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    # product = models.ForeignKey(lecture_tbl, on_delete=models.PROTECT, related_name='order_products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_item_price(self):
        return self.price * self.quantity

import hashlib
from .iamport import payments_prepare, find_transaction

class OrderTransactionManager(models.Manager):
    def create_new(self,order,amount,success=None,transaction_status=None):
        if not order:
            raise ValueError("주문 오류")

        order_hash = hashlib.sha1(str(order.id).encode('utf-8')).hexdigest()
        email_hash = str(order.email).split("@")[0]
        final_hash = hashlib.sha1((order_hash + email_hash).encode('utf-8')).hexdigest()[:10]
        merchant_order_id = "%s"%(final_hash)

        payments_prepare(merchant_order_id,amount)
        transaction = self.model(
            order=order,
            merchant_order_id=merchant_order_id,
            amount=amount
        )

        if success is not None:
            transaction.success = success
            transaction.transation_status = transaction_status

        try:
            transaction.save()
        except Exception as e:
            print("save error", e)

        return transaction.merchant_order_id

    def get_transaction(self,merchant_order_id):
        result = find_transaction(merchant_order_id)
        if result['status'] == 'paid':
            return result
        else:
            return None


class OrderTransaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    merchant_order_id = models.CharField(max_length=120, null=True, blank=True)
    transaction_id = models.CharField(max_length=120, null=True,blank=True)
    amount = models.PositiveIntegerField(default=0)
    transaction_status = models.CharField(max_length=220, null=True,blank=True)
    type = models.CharField(max_length=120,blank=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)

    objects = OrderTransactionManager()

    def __str__(self):
        return str(self.order.id)

    class Meta:
        ordering = ['-created']


def order_payment_validation(sender, instance, created, *args, **kwargs):
    if instance.transaction_id:
        import_transaction = OrderTransaction.objects.get_transaction(merchant_order_id=instance.merchant_order_id)

        merchant_order_id = import_transaction['merchant_order_id']
        imp_id = import_transaction['imp_id']
        amount = import_transaction['amount']

        local_transaction = OrderTransaction.objects.filter(merchant_order_id = merchant_order_id, transaction_id = imp_id,amount = amount).exist()

        if not import_transaction or not local_transaction:
            raise ValueError("비정상 거래입니다.")

# 결제 정보가 생성된 후에 호출할 함수를 연결해준다.
from django.db.models.signals import post_save
post_save.connect(order_payment_validation,sender=OrderTransaction)




# Create your models here.
