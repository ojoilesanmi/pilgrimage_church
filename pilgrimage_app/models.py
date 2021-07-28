from django.db import models
from datetime import datetime

class BetterNigeriaRegistration(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    contact_date = models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self):
        return self.fullname

class Messages(models.Model):
    message_title = models.CharField(max_length=256)
    cloudinary_link = models.URLField(max_length=256)
    date_released = models.DateTimeField(default=datetime.now)
    message_image = models.URLField(max_length=256)

    def __str__(self):
        return self.message_title 

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    message = models.TextField(blank=False)
    phone = models.CharField(max_length=11)
    contact_date = models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self):
        return self.fullname
