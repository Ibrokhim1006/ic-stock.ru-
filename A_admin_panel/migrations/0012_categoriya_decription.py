# Generated by Django 4.1.5 on 2023-03-16 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_admin_panel', '0011_brand_ur'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriya',
            name='decription',
            field=models.TextField(blank=True, null=True),
        ),
    ]