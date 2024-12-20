from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.views import generic
from .models import Customer, Phonemodel, Service, Ticket
from .forms import TicketForm


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


# Create a ticket
def create_ticket(request, phone_model):
    phone_model = get_object_or_404(Phonemodel, id=phone_model)

    return render(
        request,
        "book_repair/create_ticket.html",
        {"phone_model": phone_model},
    )
