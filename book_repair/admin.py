from django.contrib import admin
from .models import Ticket, Service, Phonemodel, Part
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Ticket)
class TicketAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage tickets via the admin panel
    """

    list_display = (
        'ticket_number',
        'requester',
        'imei',
        'phonemodel',
        'broken_part',
        'issue_description',
        'status',
        'created_on'
        )
    readonly_fields = ['ticket_number']
    search_fields = [
        'phonemodel__slug',
        'imei',
        'ticket_number',
        ]
    list_filter = (
        'status',
        'phonemodel__manufacturer',
        'broken_part',
        )
    summernote_fields = ('issue_description',)


@admin.register(Phonemodel)
class PhoneAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage phonemodels via the admin panel
    """

    list_display = (
        'id',
        'manufacturer',
        'series',
        )
    search_fields = [
        'slug__icontains',]
    list_filter = (
        'manufacturer',
        )


@admin.register(Part)
class PartAdmin(SummernoteModelAdmin):
    """
    Allows Admin to manage parts via the admin panel
    """
    list_display = (
        'part',
    )
    search_fields = [
        'part__icontains',
    ]


admin.site.register(Service)
