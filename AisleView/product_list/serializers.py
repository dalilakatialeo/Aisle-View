from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import Product, ProductList, Aisle, Product_Aisle

class ProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200,unique=True)

# class ProductListSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     name = serializers.CharField(max_length=200, unique=True)
#     product = serializers.ReadOnlyField(Product)
#     is_saved = serializers.BooleanField(null=False)

#     def create(self, validated_data):
#         return ProductList.objects.create(**validated_data)

# class ProductListDetailSeriali

# class AisleSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     name = serializers.CharField(max_length=200)

# class Product_AisleSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     product = serializers.ReadOnlyField(Product)
#     aisle = serializers.ReadOnlyField(Aisle)

#     def create (self, validated_data):
#         return Product_Aisle.objects.create(**validated_data)