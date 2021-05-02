# Generated by Django 3.2 on 2021-05-02 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210502_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='task_result',
        ),
        migrations.AddField(
            model_name='notification',
            name='celery_task_id',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
    ]