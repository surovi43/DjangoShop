from django.contrib import admin
from .models import User, Address, MerchantApplication


# Register User model
admin.site.register(User)

# Register Address model
admin.site.register(Address)

# Register Merchant Application model
admin.site.register(MerchantApplication)
