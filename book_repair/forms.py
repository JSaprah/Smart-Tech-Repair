from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "requester",
            "phonemodel",
            "broken_part",
            "issue_description",
            "imei"
            ]
