from django.db import models

# Create your models here.
class DonorInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ref_id = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length = 20)
    amount = models.IntegerField(default=500)
    purpose = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} payment'


    