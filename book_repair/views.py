from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import generic
from .models import Customer, Phonemodel, Service, Ticket


# Create your views here.

# Home page
def home(request):
    return render(request, "book_repair/index.html")


# Login page
def login(request):
    return render(request, "book_repair/login.html")


# Phone model
def phones_list(request):

    phones = Phonemodel.objects.all()

    context = {
        'phones': phones,

    }

    return render(request, 'book_repair/book_repair.html', context)
