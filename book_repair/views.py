from django.shortcuts import render, get_object_or_404, redirect
from .models import Phonemodel, Ticket
from .forms import CustomerForm, TicketForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.http import HttpResponseRedirect


# Create your views here.

# Home page
def home(request):
    return render(request, "book_repair/index.html")


# Login page
def login(request):
    return render(request, "book_repair/login.html")


# Returns all Phone models
def phones_list(request):

    search_phone = request.GET.get('query', '')
    if search_phone:
        phones = Phonemodel.objects.filter(
            series__icontains=search_phone,
            )
    else:
        phones = phones = Phonemodel.objects.all()

    return render(
        request,
        'book_repair/book_repair.html', {
            'phones': phones, 'search_phone': search_phone}
        )


# Ticket details page
@login_required
def ticket_details(request):
    tickets = Ticket.objects.filter(created_by=request.user)

    return render(
        request, "book_repair/ticket_details.html", {'tickets': tickets}
        )


# Edit ticket
def edit_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    return render(request, 'book_repair/edit_ticket.html', {'ticket': ticket})


# Create a ticket
@login_required
def create_ticket(request, slug):
    phone_model = get_object_or_404(Phonemodel, slug=slug)

    ticket_form = TicketForm()

    if request.method == "POST":
        ticket_form = TicketForm(data=request.POST)

        if ticket_form.is_valid():
            ticket_form.save()
            messages.add_message(request, messages.SUCCESS, "Ticket has been submitted succesfully!")
            ticket_form = TicketForm()

    else:
        ticket_form = TicketForm()

    return render(
        request,
        "book_repair/create_ticket.html",
        {
            "phone_model": phone_model,
            "ticket_form": ticket_form,

        }
    )

# Create customer

def create_customer(request):

    customer_form = CustomerForm()

    if request.method == "POST":
        customer_form = CustomerForm(data=request.POST)

        if customer_form.is_valid():
            customer_form.save()
            messages.add_message(request, messages.SUCCESS, "Ticket has been submitted succesfully!")
            customer_form = CustomerForm()

    else:
        customer_form = CustomerForm()

    return render(
        request,
        "book_repair/create_customer.html",
        {
            "customer_form": customer_form,

        }
    )
