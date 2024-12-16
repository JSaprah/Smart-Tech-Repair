from django.contrib import admin
from .models import Part, Customer, Device, Ticket, Catalogue

# Register your models here.
admin.site.register(Part)
admin.site.register(Customer)
admin.site.register(Device)
admin.site.register(Ticket)
admin.site.register(Catalogue)
