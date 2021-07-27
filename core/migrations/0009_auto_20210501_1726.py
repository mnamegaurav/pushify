# Generated by Django 3.2 on 2021-05-01 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0010_auto_20210501_1726'),
        ('core', '0008_alter_fcmtokendevice_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcmtokendevice',
            name='website',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fcmtokendevice_website', to='websites.website', verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[('FAILURE', 'FAILURE'), ('PENDING', 'PENDING'), ('RECEIVED', 'RECEIVED'), ('RETRY', 'RETRY'), ('REVOKED', 'REVOKED'), ('STARTED', 'STARTED'), ('SUCCESS', 'SUCCESS')], db_index=True, default='PENDING', help_text='Current state of the notification task being run', max_length=50, verbose_name='Notification Task State'),
        ),
    ]
