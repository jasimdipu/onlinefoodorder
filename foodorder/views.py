from django.shortcuts import render, redirect
from .models import *
from .order_form import FoodOrderForm, CreateUserForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user


# Create your views here.
@unauthenticated_user
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login is Successfull")
            return redirect('food_list')
        else:
            messages.error(request, "Not found the user")
    return render(request, 'foodorder/login.html')


@unauthenticated_user
def user_registration(request):
    user_reg_form = CreateUserForm()
    if request.method == 'POST':
        user_reg_form = CreateUserForm(request.POST)
        if user_reg_form.is_valid():
            user = user_reg_form.save()
            print(user)
            messages.success(request, "Registration is succesfull")
            return redirect('login')
        else:
            print(user_reg_form.error_messages)
            messages.error(request, "There is some problems")
            return redirect('reg')

    context = {"user_reg_form": user_reg_form}
    return render(request, 'foodorder/registration.html', context=context)


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','salesman'])
def all_foods(request):
    foods = Food.objects.all()
    context = {
        'foods': foods
    }
    return render(request, 'foodorder/foods.html', context=context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteOrder(request, order_id):
    food_order = FoodOrder.objects.get(id=order_id)
    if request.method == "POST":
        food_order.delete()
        return redirect('/')
    context = {
        'item': food_order
    }
    return render(request, 'foodorder/delete.html', context=context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer_details(request, cus_id):
    customer = Customer.objects.get(id=cus_id)
    food_orders = customer.foodorder_set.all()

    order_count = food_orders.count()

    context = {
        'customer': customer, 'food_orders': food_orders, 'order_count': order_count
    }

    return render(request, 'foodorder/order_details.html', context=context)
