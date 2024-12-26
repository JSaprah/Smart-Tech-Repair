from django.shortcuts import render, get_object_or_404
from .models import Phonemodel, Ticket
from .forms import CustomerForm, PartForm, TicketForm
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
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


# Create a ticket
@login_required
def create_ticket(request, slug):
    phone_model = get_object_or_404(Phonemodel, slug=slug)
    part_form = PartForm()
    customer_form = CustomerForm()
    ticket_form = TicketForm()

    if request.method == "POST":
        customer_form = CustomerForm(data=request.POST)
        ticket_form = TicketForm(data=request.POST)
        part_form = PartForm(data=request.POST)

        if customer_form.is_valid() and ticket_form.is_valid() and part_form.is_valid():
            customer_form.save()
            part_form.save(commit=False)

            ticket = ticket_form.save(commit=False)
            ticket.customer = customer
            ticket.broken_part = part
            ticket.save()

    else:
        customer_form = CustomerForm()
        ticket_form = TicketForm()


    return render(
        request,
        "book_repair/create_ticket.html",
        {
            "phone_model": phone_model,
            "part_form": part_form,
            "ticket_form": ticket_form,
            "customer_form": customer_form,
        }
    )


# Ticket details page
@login_required
def ticket_details(request):
    tickets = Ticket.objects.filter(created_by=request.user)

    return render(request, "book_repair/ticket_details.html", {'tickets': tickets})


# Edit ticket
def edit_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    return render(request, 'book_repair/edit_ticket.html', {'ticket': ticket})
