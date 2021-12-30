from django.db import models
from users.models import CustomUser

# Create your models here.

AISLES = [
    'FRUIT & VEG',
    'DELI',
    'MEAT',
    'FRIDGE',
    'FREEZER',
    'PASTA & SAUCES',
    'COFFEE & BISCUITS',
    'CANNED FISH & VEGGIES',
    'OILS',
    'BAKING',
    'CONFECTIONERY',
    'DRINKS',
    'ASIAN',
    'HYGIENE',
    'COOKWARE',
    'STATIONERY',
]

class Product(models.Model):
    name = models.CharField(max_length=200)
    aisle = models.CharField(
        max_length = 100,
        choices = AISLES,
        dafault = 'not_set'
    )

# class Aisle(models.Model):
#     name = models.CharField(max_length=200, unique=True)

# class Product_Aisle(models.Model):
#     product = models.ManyToManyField(Product)
#     aisle = models.ManyToManyField(Aisle)

# class ProductList(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     product = models.ManyToManyField(Product)
#     is_saved = models.BooleanField(null=False)