# Generated by Django 3.2 on 2021-05-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0012_alter_website_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(help_text='Website URL i.e. - https://example.com/', unique=True, verbose_name='Website URL'),
        ),
    ]