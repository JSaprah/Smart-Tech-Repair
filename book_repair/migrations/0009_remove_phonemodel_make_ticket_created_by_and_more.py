# Generated by Django 4.2.17 on 2024-12-25 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_repair', '0008_remove_ticket_device_remove_ticket_duration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonemodel',
            name='make',
        ),
        migrations.AddField(
            model_name='ticket',
            name='created_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='part',
            field=models.CharField(choices=[('Diagnostic Services', 'Diagnostic Services'), ('Screen Replacement', 'Screen Replacement'), ('Battery Replacement', 'Battery Replacement'), ('Charging port Replacement', 'Charging port Replacement'), ('Headphone Jack Repair', 'Headphone Jack Repair'), ('Microphone Repair', 'Microphone Repair'), ('Loudspeaker Repair', 'Loudspeaker Repair'), ('Speaker Repair', 'Speaker Repair'), ('Rear Camera Repair', 'Rear Camera Repair'), ('Front Camera Repair', 'Front Camera Repair'), ('Backglass Repair', 'Backglass Repair'), ('Rear housing Replacement', 'Rear housing Replacement')], max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='booking_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
