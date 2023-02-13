
from django.contrib import admin
from django.urls import path, include
from .views import index, register
from.views import login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'indexpage'),
    path('register', register, name='register'),
    path('login', login, name='login')
]
