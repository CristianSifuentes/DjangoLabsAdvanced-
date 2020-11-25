from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# un proxy model no genera una tabla en una base de datos

class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
