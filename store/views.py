from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.views import View
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

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
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # getting  form data that comes through post method and request object
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        mobile = postData.get('mobile')
        email = postData.get('email')
        password = make_password(postData.get('password')) # make_password hashes the password
        
        #holdin value to stay in form incase user mises some fields and refill form
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile' : mobile,
            'email': email
            }
        # saving the custom form data using named parameter
        customer = Customer(first_name=first_name,
                        last_name = last_name,
                        mobile = mobile, email= email, 
                        password = password)
        #validation 
        error_message = None
        if (not first_name):
            error_message = "First name is required !"
        elif len(first_name) < 4:
            error_message = " First name length must be greater than four characters long ."
        elif len(mobile) < 10:
            error_message = " Mobile numbers must be 10 digits long"
        elif customer.is_Exists():
            error_message = "Email address already exists ! Try with new email !!"

        if (not error_message):
            customer.register()
            return redirect('index')
        else:
            return render(request, 'register.html',{'error':error_message, 'value':value})



    

    
