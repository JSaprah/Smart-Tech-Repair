from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# from .models import Device


# Create your views here.
class booking(generic.ListView):
    # queryset = Device.objects.all()
    template_name = "part_list.html"