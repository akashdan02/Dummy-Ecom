# Generated by Django 4.1.1 on 2022-09-22 06:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand_name", models.CharField(max_length=50)),
                ("is_active", models.PositiveSmallIntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"db_table": "brand",},
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=100)),
                ("is_active", models.PositiveSmallIntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id_brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="catalog.brand"
                    ),
                ),
            ],
            options={"db_table": "category",},
        ),
        migrations.CreateModel(
            name="CatalogData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("description", models.TextField(max_length=100)),
                ("price", models.FloatField()),
                ("discountPercentage", models.FloatField()),
                ("rating", models.FloatField()),
                ("stock", models.BigIntegerField()),
                ("thumbnail", models.URLField(max_length=250)),
                (
                    "images",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.URLField(max_length=250),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                ("is_active", models.PositiveSmallIntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id_brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="catalog.brand"
                    ),
                ),
                (
                    "id_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                    ),
                ),
            ],
            options={"db_table": "catalog",},
        ),
    ]
