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

thisdict =	{
  "name": "YONG",
  "role": "M249",
  "level": 54,
  "rank":"Crown"
}
def ShowInfor(request):
    errors=[]
    if 'name' in request.GET:
        name = request.GET['name']
        if not name:
            errors.append('Enter a search term.')
        elif len(name) > 10:
            errors.append('Please enter at most 20 characters.')
        else:
            template = loader.get_template('book/infor.html')
            context={
                'name':request.GET['name'],
                'role' : thisdict["role"],
                'level' : thisdict["level"],
                'rank': thisdict["rank"]
            }
            return HttpResponse(template.render(context, request))
    return render(request, 'book/search_form.html', {'errors':errors})

def ImportFile(request):
    errors=[]
    if 'filename' in request.GET:
        filename = request.GET['filename']
        if not filename:
            errors.append('Upload a file.')
        else:
            file=open('filename', 'r')
            if file.mode=='r':
                contents = file.read()
            template = loader.get_template('book/infor.html')
            context
