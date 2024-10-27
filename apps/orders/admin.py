from django.contrib import admin
from .models import Order, OrderItem, Shipment

# Register Order model
admin.site.register(Order)

# Register OrderItem model
admin.site.register(OrderItem)

# Register Shipment model
admin.site.register(Shipment)
