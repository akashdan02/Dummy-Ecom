from django.contrib import admin
from .models import CatalogData,Brand,Category

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields=('brand_name',)
    list_display = ('brand_name','is_active','created_at','updated_at')
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields=('id_brand__brand_name','category',)
    list_display = ('id_brand','category','is_active','created_at','updated_at')
    list_filter = ('id_brand','is_active',)
    readonly_fields = ('created_at', 'updated_at')  

@admin.register(CatalogData)
class CatalogdataAdmin(admin.ModelAdmin):
    search_fields=('title','id_brand__brand_name','id_category__category',)
    list_display = ('id_brand','id_category','title','description','price','discountPercentage','rating','stock','thumbnail','images','is_active','created_at','updated_at')
    list_filter = ('id_brand','is_active',)
    readonly_fields = ('created_at', 'updated_at')  
