# Generated by Django 4.2.5 on 2024-10-01 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_product_desctiption_product_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_categoty',
            new_name='product_category',
        ),
    ]
