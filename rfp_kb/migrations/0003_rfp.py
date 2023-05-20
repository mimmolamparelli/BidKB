# Generated by Django 4.2.1 on 2023-05-20 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfp_kb', '0002_rfp_bk_product_rfp_bk_product_variant'),
    ]

    operations = [
        migrations.CreateModel(
            name='rfp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfp_name', models.CharField(max_length=200)),
                ('customer', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rfp_kb.rfp_bk')),
            ],
        ),
    ]
