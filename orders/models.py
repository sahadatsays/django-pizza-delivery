from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Order(models.Model):
    SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('EXTRA_LARGE', 'extra_large'),
        ('LARGE', 'large'),
    )

    ORDER_STATUS_LIST = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'inTransit'),
        ('DELIVERED', 'delivered'),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=SIZES, default=SIZES[0][0])
    order_status = models.CharField(
        max_length=20, choices=ORDER_STATUS_LIST, default=ORDER_STATUS_LIST[0][0])
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"<Order {self.size } by {self.customer.id}>"
