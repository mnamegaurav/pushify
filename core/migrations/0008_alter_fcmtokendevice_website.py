# Generated by Django 3.2 on 2021-05-01 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0009_alter_website_slug'),
        ('core', '0007_alter_notification_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcmtokendevice',
            name='website',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='websites.website', verbose_name='Website'),
        ),
    ]