# Generated by Django 5.1.2 on 2024-10-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0004_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="subscription",
            field=models.BooleanField(default=False, verbose_name="Признак подписки"),
        ),
    ]
