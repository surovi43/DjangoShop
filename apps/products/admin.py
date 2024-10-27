from django.contrib import admin
from .models import Product, ProductImage, Review

# Register Product model
admin.site.register(Product)

# Register ProductImage model
admin.site.register(ProductImage)

# Register Review model
admin.site.register(Review)
