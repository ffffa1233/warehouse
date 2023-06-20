from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render({}, request))