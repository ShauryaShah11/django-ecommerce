# Generated by Django 4.1.7 on 2023-03-12 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='label',
            new_name='name',
        ),
    ]
