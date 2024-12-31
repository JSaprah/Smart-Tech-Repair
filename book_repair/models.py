from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


STATUS = ((0, "Pending"), (1, "In progress"), (2, "Completed"))
MANUFACTURER = (("Apple", "Apple"), ("Samsung", "Samsung"))
PART = (
    ("Diagnostic Services", "Diagnostic Services"),
    ("Screen Replacement", "Screen Replacement"),
    ("Battery Replacement", "Battery Replacement"),
    ("Charging port Replacement", "Charging port Replacement"),
    ("Headphone Jack Repair", "Headphone Jack Repair"),
    ("Microphone Repair", "Microphone Repair"),
    ("Loudspeaker Repair", "Loudspeaker Repair"),
    ("Speaker Repair", "Speaker Repair"),
    ("Rear Camera Repair", "Rear Camera Repair"),
    ("Front Camera Repair", "Front Camera Repair"),
    ("Backglass Repair", "Backglass Repair"),
    ("Rear housing Replacement", "Rear housing Replacement"),
)


class Phonemodel(models.Model):
    """
    Stores the phonemodels

    """
    manufacturer = models.CharField(max_length=50, choices=MANUFACTURER)
    series = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        combined_slug = f"{self.manufacturer} {self.series}"
        self.slug = slugify(combined_slug)
        super(Phonemodel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.series}"


class Part(models.Model):
    """
    Stores the parts of the phone that can be repaired
    """
    part = models.CharField(max_length=50, choices=PART)

    def __str__(self):
        return f"{self.part}"


class Service(models.Model):
    """
    Combines the phonemodel and the parts
    Determines the price of the repairing
    (Unused, left it in the project for future enhancements)
    """
    phonemodel = models.ForeignKey(Phonemodel, on_delete=models.CASCADE)
    broken_part = models.ForeignKey(Part, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=50)

    def __str__(self):
        return f"{self.broken_part}"


class Ticket(models.Model):
    """
    For creating tickets for repair requests
    """
    ticket_number = models.CharField(max_length=50, unique=True, blank=True)
    phonemodel = models.ForeignKey(Phonemodel, on_delete=models.CASCADE)
    broken_part = models.ForeignKey(Part, on_delete=models.CASCADE)
    requester = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="requester_ticket", null=True, blank=True
        )
    imei = models.CharField(max_length=15)
    issue_description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

# Auto generate ticket number
    def generate_ticket_number(self):
        last_ticket = Ticket.objects.order_by('-created_on').first()

        if last_ticket:
            last_number = int(last_ticket.ticket_number.split('-')[1])
            new_number = last_number + 1
        else:
            new_number = 1
        ticket_prefix = "STR-"

        return f"{ticket_prefix}{new_number}"

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = self.generate_ticket_number()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.ticket_number}"
