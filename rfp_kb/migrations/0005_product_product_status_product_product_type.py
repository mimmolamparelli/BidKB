# Generated by Django 4.2.1 on 2023-06-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfp_kb', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
