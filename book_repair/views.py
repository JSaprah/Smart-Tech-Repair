from django.shortcuts import render, get_object_or_404, redirect
from .models import Phonemodel, Ticket
from .forms import TicketForm, EditTicketForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    """
    This view is used as an introduction to the company and the repair services
    """
    return render(request, "book_repair/index.html")


def account(request):
    """
    This view is used as for the login page
    """
    return render(request, "book_repair/account.html")


def register(request):
    """
    This view is used as for the custom register page
    The emailfield has been made mandatory for contacting purposes
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Registered succesfully, please sign in')
            return render(request, 'templates/account/login.html')

    else:
        form = CustomUserCreationForm()

    return render(request, 'book_repair/register.html', {'form': form})


def phones_list(request):
    """
    This view shows all the phonemodels to select from
    With an additional functionality to search
    """

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


@login_required
def create_ticket(request, slug):
    """
    This is the follow up view for phonemodels.
    It takes two arguments, the request and the slug.
    From here the user can fill in details for the phone and create a ticket.
    To create a ticket the user needs to be logged in
    """

    phone_model = get_object_or_404(Phonemodel, slug=slug)

    if request.method == "POST":
        ticket_form = TicketForm(data=request.POST)

        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.requester = request.user
            ticket.phonemodel = phone_model
            ticket.save()
            return redirect('confirmation', ticket_number=ticket.ticket_number)

        else:
            messages.add_message(
                request, messages.ERROR,
                'Ticket could not be created')

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


@login_required
def ticket_details(request):
    """
    This view shows an overview of the tickets created by the logged in user
    The user needs to be logged in
    """
    tickets = Ticket.objects.filter(requester=request.user)

    return render(
        request, "book_repair/ticket_details.html", {'tickets': tickets, }
        )


def edit_ticket(request, id):
    """
    This view takes the id from the ticket details.
    It allows the user to edit or delete the ticket.
    """

    ticket = get_object_or_404(Ticket, id=id)

    if request.method == 'POST':
        action = request.POST.get('action')

        ticket_form = EditTicketForm(request.POST, instance=ticket)

        if action == 'update' and ticket_form.is_valid():
            ticket_form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Ticket updated succesfully!'
                )
            return redirect('ticket_details')

        elif action == 'delete':
            ticket.delete()
            messages.add_message(
                request, messages.SUCCESS, 'Ticket deleted succesfully!'
                )
            return redirect('ticket_details')

        else:
            messages.add_message(
                request, messages.ERROR, 'Changes could not be saved'
                )
            return redirect('ticket_details')

    else:
        ticket_form = EditTicketForm(instance=ticket)

    return render(
        request, 'book_repair/edit_ticket.html', {
            'ticket_form': ticket_form, 'ticket': ticket
            }
        )


def confirmation(request, ticket_number):
    """
    This view is for confirmation for submitting requests
    """
    ticket = get_object_or_404(Ticket, ticket_number=ticket_number)

    return render(
        request, "book_repair/ticket_confirmation.html", {'ticket': ticket}
        )
