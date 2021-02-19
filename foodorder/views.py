from django.shortcuts import render
from .models import *


# Create your views here.

def dashboard(request):
    orders = FoodOrder.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    total_customers = customers.count()
    pending_del = orders.filter(status='Pending').count()
    order_delivered = orders.filter(status='Delivered').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'total_customers': total_customers,
        'pending_orders': pending_del,
        'order_delivered': order_delivered
    }
    return render(request, 'foodorder/dashboard.html', context=context)


def all_foods(request):
    foods = Food.objects.all()
    context = {
        'foods': foods
    }
    return render(request, 'foodorder/foods.html', context=context)
