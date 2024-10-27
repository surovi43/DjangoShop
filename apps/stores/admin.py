from django.contrib import admin
from .models import Store, StoreFollow, Collection


# Register Store model
admin.site.register(Store)

# Register StoreFollow model
admin.site.register(StoreFollow)

# Register Collection model
admin.site.register(Collection)
