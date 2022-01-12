from django.db.models.deletion import CASCADE
from authentication.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
  id = models.AutoField(primary_key=True, auto_created=True)
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
  title = models.CharField(max_length=64)
  content = models.CharField(max_length=164)
  price = models.DecimalField(max_digits=10, decimal_places=3)
  created_datetime = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.content
