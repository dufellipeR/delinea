from django.db.models import fields
from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
  id = serializers.ReadOnlyField()
  created_datetime = serializers.DateTimeField(read_only=True)
  class Meta:
    model= Product
    fields=[ 'id','title', 'content', 'price', 'created_datetime']
