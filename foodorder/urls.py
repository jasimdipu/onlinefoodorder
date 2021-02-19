from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('food_list', views.all_foods, name='food_list')
]
