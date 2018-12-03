from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def Home(request):
    template = loader.get_template("book/home.html")
    context={
        'pagename': 'HomePage',
    }
    return HttpResponse(template.render(context, request))
def AboutMe(request):
    return render(request, 'book/about.html')
