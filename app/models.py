from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Accountuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    aadhar_number = models.BigIntegerField()
    phone = models.CharField(max_length=10)
    account_type = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    balance = models.IntegerField()


    def __str__(self):
        return self.user.username

class Records(models.Model):
    user = models.ForeignKey("Accountuser", on_delete=models.CASCADE)
    transaction = models.CharField(max_length=30, blank=True)
    amount = models.IntegerField(blank=True)
    date = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.user.user
    
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    feedback = models.TextField()

    def __str__(self):
        return self.name
    

