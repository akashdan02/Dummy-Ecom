from django.contrib import admin

# Register your models here.
from .models import CatalogData,Brand,Category

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(CatalogData)
