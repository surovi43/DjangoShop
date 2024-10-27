import random
from django.db import models
from django.utils import timezone
from apps.users.models import User
from apps.products.models import Product


# ===================================
# Order Model
# ===================================
class Order(models.Model):
    id = models.CharField(max_length=20, primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    order_status = models.CharField(
        max_length=10,
        choices=[
            ("PENDING", "Pending"),
            ("SHIPPED", "Shipped"),
            ("DELIVERED", "Delivered"),
            ("CANCELLED", "Cancelled"),
        ],
        default="PENDING",
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_order_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_order_id():
        now = timezone.now()
        date = now.strftime("%y%m%d")
        time = now.strftime("%H%M")
        randomness = f"{random.randint(1000, 9999)}"
        return f"{date}{time}{randomness}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-order_date"]


# ===================================
# Order Item Model
# ===================================
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        db_table = "order_items"
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"


# ===================================
# Shipment Model
# ===================================
class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="shipment")
    shipping_address = models.TextField()
    shipping_charge = models.DecimalField(max_digits=8, decimal_places=2)
    shipment_method = models.CharField(max_length=50)
    shipment_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "shipments"
        verbose_name = "Shipment"
        verbose_name_plural = "Shipments"
        ordering = ["-shipment_date"]
