from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.views import View
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from store .models.orders import Order

# Create your views here.
class Index(View):
    # accessing product id user sends from clicking "add to cart" button ane managing cart
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        # print('cart',request.session['cart'])
        return redirect('indexpage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:                    
            request.session['cart'] = {} # if nothing is in cart, assign empty dictionary. revomes variable doen't exist error
        products = None
        categories = Category.collect_categories()
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_all_products_by_categoris_id(category_id)
        else:
            products = Product.get_all_products()
            # print(request.session.get('customer_email'))
    
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
            return redirect('indexpage')
        else:
            return render(request, 'register.html',{'error':error_message, 'value':value})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                # saving user id and email in server through session
                request.session['customer'] = customer.id
                return redirect('indexpage')
            else:
                error_message = " Email or Password invalid, Please check and try again !"

        else:
            error_message = " Sorry you are not registered yet...Please register first then login !"

        return render(request, 'login.html',{'error':error_message })

def logout(request):
    request.session.clear()
    return redirect('login')

class Cart(View):
    def get(self,request):
        id_list = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(id_list)
        return render(request, 'cart.html', {'products': products})


class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        # print(address,mobile, customer_id, cart, products)
        for product in products:
            order = Order(customer = Customer(id = customer_id),
                          address = address, 
                          mobile = mobile,
                          product = product,
                          price = product.price,
                          quantity = cart.get(str(product.id)))
            order.save_Order()
        request.session['cart'] = {}
        return redirect('cart')
    
class MyOrder(View):
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_customer_order(customer)
        return render(request, 'orders.html',{'orders': orders})

        
    

    
