from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
