# Generated by Django 3.0.8 on 2020-08-31 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20200831_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='domain',
            field=models.CharField(max_length=500),
        ),
    ]
