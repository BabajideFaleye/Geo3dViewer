from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView
from .models import Page, Pointcloud



# Create your views here.

def group_check(user):
    return user.groups.filter(name__in=['Bristol City Council'])


@login_required
def index(request):
    return render(request, 'viewer/index.html', context=None)


@login_required
@user_passes_test(group_check)
def sample(request):
    return render(request, 'sample.html', context=None)


class DataList(ListView):
    model = Page


@login_required
def viewer(request, pk):
    instance = get_object_or_404(Page, pk=pk)
    # print("instance is "+ str(instance))
    # print("instance is "+ str(instance.data_location))
    # print("PC is "+ str(instance.Pointcloud))
    context = {
        "test": instance,
        "pk": instance.pk,
        "data_location": instance.data_location,
        "organisation": instance.organisation.name,
        "page_name": instance.page_name,
        "Pointclouds": instance.Pointcloud.all(),

    }
    return render(request, 'viewer.html', context)

