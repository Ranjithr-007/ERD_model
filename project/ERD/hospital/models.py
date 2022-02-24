from operator import mod
from tkinter import CASCADE
from turtle import ondrag
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User, auth, AbstractUser
from django.db.models import Count
from datetime import date
from django.core.validators import MaxValueValidator
from django.forms import CharField
from django.utils import timezone

USER_CHOICES = [
    ('D', 'Doctor'),
    ('P', 'Patient'),
    ('R', 'Receptionist'),
    ('HR', 'HR')
]

class User(AbstractUser):
    user_type = models.CharField(choices=USER_CHOICES, max_length=2)

    def is_doctor(self):
        if self.user_type == 'D':
            return True
        else:
            return False

    def is_patient(self):
        if self.user_type == 'P':
            return True
        else:
            return False

    def is_receptionist(self):
        if self.user_type == 'R':
            return True
        else:
            return False

    def is_HR(self):
        if self.user_type == 'HR':
            return True
        else:
            return False

    class Meta:
        ordering = ('id',)


class Patient(models.Model):
    mrd_number = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()

class Doctor(models.Model):
    name = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    specialties = models.CharField(max_length=1000)
    education = models.CharField(max_length=1000)
    hospitals = models.CharField(max_length=1000)
    description = models.TextField(null=True)

class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(Patient, default='SOME STRING',on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return "User - {} Doc- {} At {} {}".format(self.patient, self.doctor, self.date, self.time)
    

class Feedback(models.Model):
    patient = models.ForeignKey(Patient,default='SOME STRING' ,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=400)

class Leave(models.Model):
    Leave_ID = models.CharField(max_length=5, default=" ")
    name = models.ForeignKey('User',choices=USER_CHOICES, on_delete=models.CASCADE)
    l = (
        ("Paid","Paid"),("Non-Paid","Non-Paid")
    ) 
    Leave_Type = models.CharField(max_length=10, choices= l, default="Non-Paid")
    m = (
        ("January","January"),("February","February"),("March","March"),("April","April"),("May","May"),("June","June"),("July","July"),("August","August"),("September","September"),("October","October"),("November","November"),("December","december")
    )
    Month = models.IntegerField(MaxValueValidator(2), choices= m)
    Year = models.IntegerField(MaxValueValidator(4))
    Start_Date = models.DateField(default=timezone.now)
    End_Date = models.DateField(null=True, blank = True)
    Reason = models.CharField(max_length=500)
    s = (
       ("Accepted","Accepted"),("Pending","Pending"),("Canceled","Canceled")
    )
    Status = models.CharField(max_length=10, choices= s, default="Pending")


    def __str__(self):
        return str(self.name)