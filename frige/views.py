from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import FrigeItem
from django.utils import timezone, dateformat
from datetime import datetime


# Create your views here.
def index(request):
    #myFrigeItem = FrigeItem.objects.all().order_by('-quantity').values()
    myFrigeItem = FrigeItem.objects.all().values()
    template = loader.get_template('frige/frige.html')
    context = {
        'myFrigeItem': myFrigeItem,
        #'myFrigeItem_Idx': 1,
    }
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

