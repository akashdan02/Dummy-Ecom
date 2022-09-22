from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length = 50)
    is_active = models.PositiveSmallIntegerField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "brand"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    is_active = models.PositiveSmallIntegerField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "category"


class CatalogData(models.Model):
    id = models.AutoField(primary_key=True)
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    price = models.FloatField()
    discountPercentage = models.FloatField()
    rating = models.FloatField()
    stock = models.BigIntegerField()
    thumbnail = models.URLField(max_length=250)
    images = ArrayField(models.CharField(max_length=250), blank=True, default=list)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "catalog"