from django.shortcuts import render, redirect
from .models import *
from .order_form import FoodOrderForm
from django.forms import inlineformset_factory


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


def createFoodOrder(request, cus_id):
    OrderFoodFromSet = inlineformset_factory(Customer, FoodOrder, fields=('food', 'status'))
    customer = Customer.objects.get(id=cus_id)
    formset = OrderFoodFromSet(instance=customer)
    # form = OrderFoodFromSet(initial = {'customer':customer})
    form = FoodOrderForm()
    if request.method == "POST":
        # form = FoodOrderForm(request.POST)
        formset = OrderFoodFromSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {
        'formset': formset
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


def customer_details(request, cus_id):
    customer = Customer.objects.get(id=cus_id)
    food_orders = customer.foodorder_set.all()

    order_count = food_orders.count()

    context = {
        'customer': customer, 'food_orders': food_orders, 'order_count': order_count
    }

    return render(request, 'foodorder/order_details.html', context=context)
