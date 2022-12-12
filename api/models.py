from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shifts(models.Model):     # This model will contain all the shift in which yoga classes provide class. For example 6AM-7AM
    shift = models.CharField(max_length=25, null=True, blank=True)


class Userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)   # user is foreign key from Auth User model(Django Authentivation model)
    dob = models.DateField()         # Person age to be filled
    phone = models.BigIntegerField()        # Person phone number to be stored
    registration_timestamp = models.DateTimeField(auto_now_add=True)        # Registration date and time of the person


class PaymentStatus(models.Model):      # It contains payment of all User month wise
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)        
    month_cycle = models.CharField(max_length=10)       # It contains month and year of the payment. For example 11/22 11 is month and 22 is year
    shift = models.ForeignKey(Shifts, on_delete=models.SET_NULL, null=True)    # Shift in which Person will come to gym. It is Foreign key from the model Shifts
    payment_time = models.DateTimeField(auto_now_add=True)      # It contains time of the payment done
