# Generated by Django 3.2 on 2021-04-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0006_rename_name_website_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Website title'),
        ),
    ]
