# Generated by Django 4.2.17 on 2024-12-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_repair', '0011_phonemodel_slug_alter_phonemodel_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
