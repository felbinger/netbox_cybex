# Generated by Django 4.2.9 on 2024-02-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_credentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
