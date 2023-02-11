from django.shortcuts import render
from django.views import View
from .models.product import Product
from .models.category import Category

# Create your views here.
def index(request):
    products = None
    categories = Category.collect_categories()
    category_id = request.GET.get('category')
    if category_id:
        products = Product.get_all_products_by_categoris_id(category_id)
    else:
           products = Product.get_all_products()
 
    return render(request, 'index.html', {'products': products, 'categories':categories})


def register(request):
    return render(request, 'register.html')
    
