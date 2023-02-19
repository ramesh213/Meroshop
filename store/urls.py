
from django.contrib import admin
from django.urls import path, include
from .views import Index, register, Cart
from.views import login
from.views import logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name = 'indexpage'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name = 'cart')
]
