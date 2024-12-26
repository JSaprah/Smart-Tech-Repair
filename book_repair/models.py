from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, "Pending"), (1, "In progress"), (2, "Completed"))
MANUFACTURER = (("Apple", "Apple"), ("Samsung", "Samsung"))
# MAKE = ((1, "iPhone 16"), (2, "iPhone 15"))
# REPAIR_DURATION = 1
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


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Phonemodel(models.Model):
    manufacturer = models.CharField(max_length=50, choices=MANUFACTURER)
    series = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        combined_slug = f"{self.manufacturer} {self.series}"
        self.slug = slugify(combined_slug)
        super(Phonemodel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.manufacturer} {self.series}"


class Service(models.Model):
    phonemodel = models.ForeignKey(Phonemodel, on_delete=models.CASCADE)
    part = models.CharField(max_length=50, choices=PART)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=50)

    def __str__(self):
        return f"{self.part}"


class Ticket(models.Model):
    phonemodel = models.ForeignKey(Phonemodel, on_delete=models.CASCADE)
    broken_part = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    imei = models.CharField(max_length=15)
    issue_description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=50, unique=True, blank=True)

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

    def __str__(self):
        return f"{self.ticket_number}{self.phonemodel} {self.broken_part} for {self.customer}"
