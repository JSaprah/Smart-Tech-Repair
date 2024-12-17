from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Part


# Create your views here.
class booking(generic.ListView):
    queryset = Part.objects.all()
    template_name = "part_list.html"
