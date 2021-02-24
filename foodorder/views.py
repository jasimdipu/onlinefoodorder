from django.shortcuts import render, redirect
from .models import *
from .order_form import FoodOrderForm


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


def createFoodOrder(request):
    form = FoodOrderForm()
    if request.method == "POST":
        form = FoodOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'foodorder/foodorderform.html', context=context)


def updateFoodOrder(request, order_id):
    food_order = FoodOrder.objects.get(id=order_id)
    form = FoodOrderForm(instance=food_order)
    if request.method == "POST":
        form = FoodOrderForm(request.POST, instance=food_order)  # global variable/instance/attr
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request, 'foodorder/foodorderform.html', context=context)


def deleteOrder(request, order_id):
    food_order = FoodOrder.objects.get(id=order_id)
    if request.method == "POST":
        food_order.delete()
        return redirect('/')
    context = {
        'item': food_order
    }
    return render(request, 'foodorder/delete.html', context=context)
