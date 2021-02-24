from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('food_list', views.all_foods, name='food_list'),
    path('food_order', views.createFoodOrder, name='food_order'),
    path('update_food_order/<str:order_id>/', views.updateFoodOrder, name='update_food_order'),
    path('delete_food_order/<str:order_id>/', views.deleteOrder, name='delete_food_order')
]
