from django.contrib import admin
from .models import Coupon, Payment, CartItem

# Register Coupon model
admin.site.register(Coupon)

# Register Payment model
admin.site.register(Payment)

# Register CartItem model
admin.site.register(CartItem)
