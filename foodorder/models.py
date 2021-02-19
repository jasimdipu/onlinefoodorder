from django.db import models

# Create your models here.

CATEGORY = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor')
)

STATUS = (
    ('Pending', 'Pending'),
    ('Out of Delivery', 'Out of Delivery'),
    ('Delivered', 'Delivered')
)


class Customer(models.Model):
    name = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name


class Food(models.Model):
    food_name = models.CharField(max_length=200, null=False)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    price = models.FloatField(null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.food_name


class FoodOrder(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    food = models.ForeignKey(Food, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.food.food_name
