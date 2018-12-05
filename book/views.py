from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def Home(request):
    template = loader.get_template("book/home.html")
    context={
        'pagename': 'PLAYERUNKNOWN\'S BATTLEGROUNDS',
    }
    return HttpResponse(template.render(context, request))

def AboutMe(request):
    return render(request, 'book/about.html')

def SearchForm(request):
    return render(request, 'book/search_form.html')

def info(request):
    if 'search' in request.GET:
        message = 'You searched for: %r' % request.GET['search']
    else
        message = 'You submitted an empty form.'
    return HttpResponse(message)
