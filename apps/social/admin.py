from django.contrib import admin
from .models import WishlistItem, Post, PostImage, PostLike

# Register WishlistItem model
admin.site.register(WishlistItem)

# Register Post model
admin.site.register(Post)

# Register PostImage model
admin.site.register(PostImage)

# Register PostLike model
admin.site.register(PostLike)
