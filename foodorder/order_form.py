from django.forms import ModelForm
from .models import FoodOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FoodOrderForm(ModelForm):
    class Meta:
        model = FoodOrder
        fields = '__all__'
        # fields = ['customer', 'food', 'status']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #fields = "__all__"
