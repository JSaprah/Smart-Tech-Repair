from django.contrib import admin
from .models import Customer, Ticket, Service, Phonemodel
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Ticket)
class PostAdmin(SummernoteModelAdmin):

    list_display = (
        'ticket_number',
        'imei',
        'customer',
        'phonemodel',
        'broken_part',
        'booking_date',
        'issue_description',
        'status',
        'created_on'
        )
    readonly_fields = ['ticket_number']
    search_fields = [
        'phonemodel__make__icontains',
        'phonemodel__series',
        'customer__first_name__icontains',
        'customer__last_name__icontains']
    list_filter = (
        'status',
        'phonemodel__manufacturer',
        'booking_date'
        )
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('issue_description',)


# Register your models here.
admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Phonemodel)
