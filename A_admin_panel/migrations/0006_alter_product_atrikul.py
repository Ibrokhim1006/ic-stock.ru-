# Generated by Django 4.1.5 on 2023-01-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_admin_panel', '0005_alter_categoriya_img_categoriya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='atrikul',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]