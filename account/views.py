from django.shortcuts import render
from .models import *



def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()

    total_order = order.count()
    order_d = order.filter(status = 'Delivered').count()
    order_p = order.filter(status = 'Pending').count()
    
    context = {'customer': customer,'order':order,'total_order':total_order,'order_d':order_d,'order_p':order_p}

    return render(request, 'dashboard.html',context )

def customer(request,pk):
    
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    order_count = order.count()

    context = {'customer':customer, 'order':order,'order_count':order_count}
    
    return render(request, 'customer.html',context)

def products(request):
    products = Product.objects.all()
    
    return render(request, 'product.html',{'products': products})