from .forms import OrderForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import *

# Create your views here.


# relative path of template is from templates *don't include templates in path*
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {'orders': orders, 'customers': customers}

    return render(request, 'home/home.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def customer(request, id):
    customer = Customer.objects.get(id=id)
    context = {'customer': customer}
    return render(request, 'customer/customer.html', context)


# CRUD FUNCTIONALITY
def create_order(request):
    form = OrderForm()
    context = {'form': form}
    if request.method == 'POST':
        print('Printing post:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'Order/order.html', context)


def update_order(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    context = {'form': form}
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'Order/order.html', context)


def delete_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'order': order}
    return render(request, 'Order/delete.html', context)


def contact(request):
    return HttpResponse('about')
