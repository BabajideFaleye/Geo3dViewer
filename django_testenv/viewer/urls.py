from .import views
from django.urls import path
from django.urls import re_path as url
from . views import DataList, viewer, sample

urlpatterns = [
    path('', views.index, name='index'),
    path('sample', views.sample, name='sample'),
    path('DataList', DataList.as_view(), name='DataList'),
    url(r'^viewer/(?P<pk>\d+)/$', viewer),
]
