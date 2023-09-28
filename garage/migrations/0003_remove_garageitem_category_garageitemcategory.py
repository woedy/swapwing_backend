# Generated by Django 4.2 on 2023-07-29 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("garage", "0002_rename_cost_in_credits_garageitem_duration_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="garageitem",
            name="category",
        ),
        migrations.CreateModel(
            name="GarageItemCategory",
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
                (
                    "category_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "item",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item_category",
                        to="garage.garageitem",
                    ),
                ),
            ],
        ),
    ]