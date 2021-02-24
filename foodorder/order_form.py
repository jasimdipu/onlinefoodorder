from django.forms import ModelForm
from .models import FoodOrder


class FoodOrderForm(ModelForm):
    class Meta:
        model = FoodOrder
        fields = '__all__'
        # fields = ['customer', 'food', 'status']
