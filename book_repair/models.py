from django.db import models
from django.contrib.auth.models import User

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
    ("1", "1")
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
    series = models.CharField(max_length=50)
    make = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.manufacturer} {self.series} {self.make}"


class Service(models.Model):
    phonemodel = models.ForeignKey(Phonemodel, on_delete=models.CASCADE)
    part = models.CharField(max_length=50, choices=PART)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.part}"


#class Device(models.Model):
 #   phonemodel = models.ForeignKey(Phonemodel, on_delete=models.CASCADE)
 #   customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 #   imei = models.CharField(max_length=15, unique=True)
  #  issue_description = models.TextField()

 #   def __str__(self):
  #      return f"{self.phonemodel} {self.imei} - {self.customer}"


class Ticket(models.Model):
    phonemodel = models.ForeignKey(Phonemodel, on_delete=models.CASCADE)
    broken_part = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    imei = models.CharField(max_length=15, unique=True)
    issue_description = models.TextField()