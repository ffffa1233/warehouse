from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import FrigeItem
from django.utils import timezone, dateformat
import datetime
import time

frige_start_year = 2022
frige_start_month = 1

# Create your views here.
def index(request):
    myFrigeItemAll = FrigeItem.objects.all().order_by('date_add_frige').values()
    myFrigeItemForHtml = {}
    myFrigeItemForHtml_Ice = {}
    dt_now = datetime.datetime.now()
    for frigeItem in myFrigeItemAll:
        frigeItemDateType = time.strptime(frigeItem['date_add_frige'], '%Y-%m-%d')
        frigeItemKey = str(frigeItemDateType.tm_year) + '년 ' + str(frigeItemDateType.tm_mon) + '월'
        if frigeItem['freezing'] == '냉장':
            if frigeItemKey not in myFrigeItemForHtml:
                myFrigeItemForHtml[frigeItemKey] = []
            myFrigeItemForHtml[frigeItemKey].append(frigeItem)
        else:
            if frigeItemKey not in myFrigeItemForHtml_Ice:
                myFrigeItemForHtml_Ice[frigeItemKey] = []
            myFrigeItemForHtml_Ice[frigeItemKey].append(frigeItem)

        #print(dateStr['item'] + ":", end='')
        #print(time.strptime(dateStr['date_add_frige'], '%Y-%m-%d').tm_mon)
        #print(dateStr)
    #myFrigeItem = []
    #myFrigeItem_year_month = []
    #for year in range(frige_start_year, dt_now.year+1):
    #    for month in range(1,13):
    #        year_month_str = str(year)+"-0"+str(month)
    #        myFrigeItem_year_month.append(year_month_str)
    #        myFrigeItem.append(FrigeItem.objects.filter(date_add_frige__contains=year_month_str))
            #print(myFrigeItem[year_month_str])
    template = loader.get_template('frige/frige.html')
    context = {
        'myFrigeItem': myFrigeItemForHtml.items(),
        'myFrigeItem_Ice': myFrigeItemForHtml_Ice.items(),
    #    'myFrigeItem_year_month' : myFrigeItem_year_month,
        #'myFrigeItem_Idx': 1,
    }
    #print(myFrigeItemForHtml)
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('frige/add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    item = request.POST['item']
    date_input = datetime.strftime(timezone.now(), '%Y-%m-%d %H:%M:%s')
    date_add_frige = request.POST['date_add_frige']
    freezing = request.POST['freezing']
    date_expire = request.POST['date_expire']
    quantity = request.POST['quantity']
    source = request.POST['source']
    etc = request.POST['etc']
    frigeItem = FrigeItem(
        item=item,
        date_input=date_input,
        date_add_frige=date_add_frige,
        freezing=freezing,
        date_expire=date_expire,
        quantity=quantity,
        source=source,
        etc=etc
    )
    frigeItem.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, frige_id):
    deleteItem = FrigeItem.objects.get(id=frige_id)
    deleteItem.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, frige_id):
    updateItem = FrigeItem.objects.get(id=frige_id)
    template = loader.get_template('frige/update.html')
    return HttpResponse(template.render({'updateItem': updateItem}, request))


def updaterecord(request, frige_id):
    item = request.POST['item']
    date_input = datetime.strftime(timezone.now(), '%Y-%m-%d %H:%M:%s')
    date_add_frige = request.POST['date_add_frige']
    freezing = request.POST['freezing']
    date_expire = request.POST['date_expire']
    quantity = request.POST['quantity']
    source = request.POST['source']
    etc = request.POST['etc']

    updateItem = FrigeItem.objects.get(id=frige_id)
    updateItem.item = item
    updateItem.date_input = date_input
    updateItem.date_add_frige = date_add_frige
    updateItem.freezing = freezing
    updateItem.date_expire = date_expire
    updateItem.quantity = quantity
    updateItem.source = source
    updateItem.etc = etc
    updateItem.save()
    return HttpResponseRedirect(reverse('index'))

