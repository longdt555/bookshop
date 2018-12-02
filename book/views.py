from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('book/index.html')
    context = {
        'name':'Yong',
    }
    return HttpResponse(template.render(context, request))

#
# def showName(request):
#     template = loader.get_template('book/name.html')
#     context= {
#         'yourname':'Long'
#     }
#     return HttpResponse(template.render(context,request))
