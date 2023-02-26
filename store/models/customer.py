from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=300)

    def register(self):
        self.save()

    def is_Exists(self):
        if Customer.objects.all().filter(email =self.email):
            return True
        else:
            return False
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

    def __str__(self):
        return self.first_name +" "+ self.last_name
