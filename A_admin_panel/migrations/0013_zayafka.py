# Generated by Django 4.1.5 on 2023-03-22 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_admin_panel', '0012_categoriya_decription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zayafka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=250, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=250, null=True)),
                ('e_phone', models.CharField(blank=True, max_length=250, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
