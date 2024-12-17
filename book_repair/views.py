from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import generic
from .models import Customer


# Create your views here.
def customer_list(request):
    customers = Customer.objects.all()

    context = {
        'customers': customers,
    }

    return render(request, 'book_repair/customer_list.html', context)
