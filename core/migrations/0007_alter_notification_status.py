# Generated by Django 3.2 on 2021-05-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210430_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[('1', 'SUCCESS'), ('2', 'FAILURE'), ('3', 'PENDING'), ('4', 'STARTED'), ('5', 'RETRY')], default='3', editable=False, max_length=2, verbose_name='Notification Status'),
        ),
    ]
