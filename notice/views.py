from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import NoticeItem
import datetime

# Create your views here.
def index(request):
    myNoticeItemAll = NoticeItem.objects.all().values()
    template = loader.get_template('notice/notice.html')
    context = {
        'myNoticeItem': myNoticeItemAll,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('notice/add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    title = request.POST['title']
    date_input = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%s')
    category = request.POST['category']
    context = request.POST['context']
    noticeItem = NoticeItem(
        title=title,
        date_input=date_input,
        category=category,
        context=context
    )
    noticeItem.save()
    return HttpResponseRedirect(reverse('notice:index'))


def delete(request, notice_id):
    deleteItem = NoticeItem.objects.get(id=notice_id)
    deleteItem.delete()
    return HttpResponseRedirect(reverse('notice:index'))


def update(request, notice_id):
    updateItem = NoticeItem.objects.get(id=notice_id)
    template = loader.get_template('notice/update.html')
    return HttpResponse(template.render({'updateItem': updateItem}, request))


def updaterecord(request, notice_id):
    title = request.POST['title']
    date_input = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%s')
    category = request.POST['category']
    context = request.POST['context']
    noticeItem = NoticeItem.objects.get(id=notice_id)
    noticeItem.title = title
    noticeItem.date_input = date_input
    noticeItem.category = category
    noticeItem.context = context
    noticeItem.save()
    return HttpResponseRedirect(reverse('notice:index'))

