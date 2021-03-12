from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('food_list', views.all_foods, name='food_list'),
    path('food_order/<str:cus_id>', views.createFoodOrder, name='food_order'),
    path('update_food_order/<str:order_id>/', views.updateFoodOrder, name='update_food_order'),
    path('delete_food_order/<str:order_id>/', views.deleteOrder, name='delete_food_order'),
    path('cus_details/<str:cus_id>/', views.customer_details, name='cus_details'),

    path('login', views.user_login, name="login"),
    path('reg', views.user_registration, name='reg'),
    path('logout', views.user_logout, name='logout'),
]
