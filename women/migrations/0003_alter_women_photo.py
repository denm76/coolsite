# Generated by Django 3.2.7 on 2021-09-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_alter_women_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='photo',
            field=models.ImageField(default='', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
