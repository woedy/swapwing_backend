# Generated by Django 4.2 on 2023-07-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="personalinfo",
            name="is_online",
            field=models.BooleanField(default=False),
        ),
    ]
