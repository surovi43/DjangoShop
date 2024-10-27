from django.db import models
from apps.users.models import User
from apps.stores.models import Store
from apps.products.models import Product


# ===================================
# Wishlist Item Model
# ===================================
class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "wishlist_items"
        verbose_name = "Wishlist Item"
        verbose_name_plural = "Wishlist Items"
        unique_together = ("user", "product")


# ===================================
# Post and Post Interaction Models
# ===================================
class Post(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=True, null=True)
    total_likes = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, through="PostLike", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-created_at",)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="post_images/")

    class Meta:
        db_table = "post_images"
        verbose_name = "Post Image"
        verbose_name_plural = "Post Images"


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "post_likes"
        verbose_name = "Post Like"
        verbose_name_plural = "Post Likes"
        unique_together = ("post", "user")
