from django.db import models
from time import timezone

# Create your models here.

# FrigeItem Attribute :
# Item : 냉장고에 들어간 물품(Mandantory)
# date_input : 웹페이지에 쓴 날짜(Auto)
# date_add_frige : 냉장고에 들어간 실제 날짜(Mandantory)
# freezing : 냉장고/냉동고.. null or !yes : 냉장고, yes : 냉동고
# date_expire : 유통기한(Optional)
# quantity : 수량(Optional)
# source : 어디서 얻게 된 것인지(Optional)
# etc : 기타(Optional)
class FrigeItem(models.Model):
    item = models.CharField(max_length=50)
    date_input = models.CharField(max_length=50, null=True)
    date_add_frige = models.CharField(max_length=50, null=True)
    freezing = models.CharField(max_length=50, null=True)
    date_expire = models.CharField(max_length=50, null=True)
    quantity = models.CharField(max_length=50, null=True)
    source = models.CharField(max_length=200, null=True)
    etc = models.CharField(max_length=200, null=True)
