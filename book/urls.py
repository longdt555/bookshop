from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^home/$', views.Home),
    url(r'^about/$', views.AboutMe),
    url(r'^search/$', views.SearchForm),
    url(r'^infor/$', views.ShowInfor),
]
