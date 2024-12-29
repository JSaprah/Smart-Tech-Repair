from django.shortcuts import render, get_object_or_404, redirect
from .models import Phonemodel, Ticket
from .forms import TicketForm
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
            slug__icontains=search_phone,
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
    tickets = Ticket.objects.filter(requester=request.user)

    return render(
        request, "book_repair/ticket_details.html", {'tickets': tickets}
        )


# Create a ticket
@login_required
def create_ticket(request, slug):
    phone_model = get_object_or_404(Phonemodel, slug=slug)

    if request.method == "POST":
        ticket_form = TicketForm(data=request.POST)

        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.requester = request.user
            ticket.phone_model = phone_model
            ticket.save()
            ticket_number = ticket.ticket_number
            return redirect('confirmation', ticket_number=ticket_number)

    else:
        ticket_form = TicketForm()

    return render(
        request,
        "book_repair/create_ticket.html",
        {
            "ticket_form": ticket_form,
            "phone_model": phone_model,
        }
    )


# Edit ticket
def edit_ticket(request, id):

    ticket = get_object_or_404(Ticket, id=id)

    if request.method == 'POST':
        action = request.POST.get('action')

        ticket_form = TicketForm(request.POST, instance=ticket)

        if action == 'update' and ticket_form.is_valid():
            ticket_form.save()
            return redirect('ticket_details')

        elif action == 'delete':
            ticket.delete()
            return redirect('ticket_details')

    else:
        ticket_form = TicketForm(instance=ticket)

    return render(
        request, 'book_repair/edit_ticket.html', {'ticket_form': ticket_form, 'ticket': ticket}
        )


# Confirmation
def confirmation(request, ticket_number):

    ticket = get_object_or_404(Ticket, ticket_number=ticket_number)

    return render(
        request, "book_repair/ticket_confirmation.html", {'ticket': ticket}
        )
