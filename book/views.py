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
#
# def ShowInfor(request):
#     if 'name' in request.GET:
#         template = loader.get_template('book/infor.html')
#         context={
#             'name':request.GET['name'],
#             'role':request.GET['role'],
#             'level':request.GET['level'],
#             'rank':request.GET['rank'],
#         }
#     else:
#         return render(request, 'book/search_form.html')
#     return HttpResponse(template.render(context, request))
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
