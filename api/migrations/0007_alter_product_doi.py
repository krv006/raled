# Generated by Django 5.0.6 on 2024-05-22 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_product_best'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='doi',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
