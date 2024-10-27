from django.db import models
from apps.users.models import User
from apps.products.models import Product


# ===================================
# Coupon Model
# ===================================
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    discount_type = models.CharField(
        max_length=20, choices=[("PERCENT", "Percent"), ("FIXED", "Fixed")]
    )
    discount_value = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_uses = models.PositiveIntegerField(default=0)
    uses_per_user = models.PositiveIntegerField(default=1)
    min_order_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = "coupons"
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"


# ===================================
# Payment Model
# ===================================
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, unique=True)
    transaction_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "payments"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"


# ===================================
# Cart Model
# ===================================
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "cart_items"
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
        unique_together = ("user", "product")
