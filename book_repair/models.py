from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "In progress"), (2, "Completed"))
# MANUFACTURER = ((0, "Apple"), (1, "Samsung"))
# MAKE = ((1, "iPhone 16"), (2, "iPhone 15"))
# REPAIR_DURATION = 1
PART = (
    (1, "Diagnostic Services"),
    (2, "Screen Replacement"),
    (3, "Battery Replacement"),
    (4, "Charging port Replacement"),
    (5, "Headphone Jack Repair"),
    (6, "Microphone Repair"),
    (7, "Loudspeaker Repair"),
    (8, "Speaker Repair"),
    (9, "Rear Camera Repair"),
    (10, "Front Camera Repair"),
    (11, "Backglass Repair"),
    (12, "Rear housing Replacement"),
)


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    # requester = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Device(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=50)
    make = models.CharField(max_length=100)
    imei = models.CharField(max_length=15, unique=True)
    issue_description = models.TextField()
    # manufacturer = models.IntegerField(choices=MANUFACTURER) #brand

    def __str__(self):
        return f"{self.manufacturer} {self.make} - {self.customer}"


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    booking_date = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    # ticketnumber = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f"Repair for{self.device} {self.status}"

