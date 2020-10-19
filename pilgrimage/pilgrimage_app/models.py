from django.db import models
from datetime import datetime

class BetterNigeriaRegistration(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    contact_date = models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self):
        return self.fullname