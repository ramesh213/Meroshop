from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='product_image/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoris_id(category_id):
        if category_id:
             return Product.objects.filter(category = category_id)
        else:
            Product.get_all_products()



