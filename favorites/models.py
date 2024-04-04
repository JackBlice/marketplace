from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class FavoriteItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
