# Generated by Django 4.1.5 on 2023-02-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_admin_panel', '0005_seocategory_alter_product_amunt_seocontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amunt',
            field=models.CharField(blank=True, default='440178705', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='seocontent',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
