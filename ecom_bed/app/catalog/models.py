from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Brand(models.Model):
    brand_name = models.CharField(max_length = 50)

    is_active = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "brand"

    def __str__(self):
        return f'{str(self.id)} - {self.brand_name}'

class Category(models.Model):
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    is_active = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return f'{str(self.id)} - {self.id_brand.brand_name} -{self.category}'

class CatalogData(models.Model):
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    price = models.FloatField()
    discountPercentage = models.FloatField()
    rating = models.FloatField()
    stock = models.BigIntegerField()
    thumbnail = models.URLField(max_length=250)
    images = ArrayField(models.URLField(max_length=250), blank=True, default=list)

    is_active = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "catalog"
    
    def __str__(self):
         return f'{str(self.id)} - {self.title}'

