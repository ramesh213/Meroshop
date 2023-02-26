from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, default=" ", null= True, blank=True)
    mobile = models.CharField(max_length=15, default = " ", blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.BooleanField(default= False)
    date = models.DateTimeField(default=datetime.datetime.today)
    
    def save_Order(self):
        self.save()  

    @staticmethod
    def get_customer_order(customer_id):
        return Order.objects.filter(customer = customer_id)