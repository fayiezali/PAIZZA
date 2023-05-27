from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate
from home.models import *


def home(request):
    pizzas = Pizza.objects.all()
    context= { 'pizzas' : pizzas}
    return render (request , 'home/index.html' , context)
    # return render (request , 'home/home.html' , context)


def about(request):
    context= { }
    return render (request , 'home/about.html' , context)


def remove_cart_items(request , cart_item_uid):
    try:
        CartItems.objects.get(uid=cart_item_uid).delete()
        return redirect('/cart/')
    except Exception as e:
        print(e)


def login_page(request):
    return render(request , 'register_page.html')


def register_page(request):
    return render(request , 'register_page.html')

def add_cart(request , pizza_uid):
    user = request.user
    pizza_obj = Pizza.objects.get(uid = pizza_uid)
    cart , _ = Cart.objects.get_or_create(user = user , is_paid = False)
    cart_items = CartItems.objects.create(cart = cart , pizza = pizza_obj)
    return redirect('/')

def cart(request):
    cart = Cart.objects.get(is_paid = False , user = request.user)
    context = {'carts' : cart}
    return render(request , 'home/cart.html' , context)


