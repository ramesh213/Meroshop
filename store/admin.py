from django.contrib import admin
from .models.product import Product
from .models.category import Category
from.models.customer import Customer


# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'description', 'image']


class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'mobile', 'email', 'password']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
