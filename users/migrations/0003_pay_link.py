# Generated by Django 5.1.2 on 2024-10-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_pay"),
    ]

    operations = [
        migrations.AddField(
            model_name="pay",
            name="link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
    ]
