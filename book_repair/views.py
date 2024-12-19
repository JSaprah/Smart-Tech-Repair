from django.shortcuts import render, get_object_or_404
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


def booking_details(request, id):

    booking = get_object_or_404(Customer, id=id)
    context = {
        'booking': booking
        }

    return render(request, 'book_repair/book_repair_details.html', context)