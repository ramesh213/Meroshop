from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


    @staticmethod
    def collect_categories():
        return Category.objects.all()
        
    def __str__(self):
        return self.name
