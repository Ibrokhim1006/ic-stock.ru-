# Generated by Django 4.1.5 on 2023-02-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_admin_panel', '0002_seomap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amunt',
            field=models.CharField(blank=True, default='98344', max_length=250, null=True),
        ),
    ]
