# Generated by Django 4.2.6 on 2023-10-16 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_product_disc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='disc',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
