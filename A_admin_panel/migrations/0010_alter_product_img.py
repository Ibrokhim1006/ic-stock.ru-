# Generated by Django 4.1.5 on 2023-01-30 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_admin_panel', '0009_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]
