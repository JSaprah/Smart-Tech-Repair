# Generated by Django 4.2.17 on 2024-12-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_repair', '0013_ticket_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='imei',
            field=models.CharField(max_length=15),
        ),
    ]