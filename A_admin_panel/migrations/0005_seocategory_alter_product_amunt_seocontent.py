# Generated by Django 4.1.5 on 2023-02-17 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('A_admin_panel', '0004_alter_product_amunt'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='amunt',
            field=models.CharField(blank=True, default='956023262', max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='SeoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('id_seo_catgeory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A_admin_panel.seocategory')),
            ],
        ),
    ]
