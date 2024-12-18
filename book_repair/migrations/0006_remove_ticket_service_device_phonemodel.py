# Generated by Django 4.2.17 on 2024-12-18 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_repair', '0005_alter_service_part'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='service',
        ),
        migrations.AddField(
            model_name='device',
            name='phonemodel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book_repair.phonemodel'),
            preserve_default=False,
        ),
    ]