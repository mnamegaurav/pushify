# Generated by Django 3.2 on 2021-04-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0007_alter_website_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]
