from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Part


# Create your views here.
class Booking(generic.ListView):
    model = Part
