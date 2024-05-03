from django.db import models
from ManagerApp.models import *

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=150)
    age = models.IntegerField()
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user'


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    package_id = models.ForeignKey(Packages,on_delete=models.CASCADE)
    booking_date = models.DateField(auto_created=True)

    class Meta:
        db_table = 'bookings'

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    package_id = models.ForeignKey(Packages,on_delete=models.CASCADE)
    review_description = models.CharField(max_length=2000)

    class Meta:
        db_table = 'reviews'


class UserEnquieries(models.Model):
    enquiry_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()


    class Meta:
        db_table = 'enquire'