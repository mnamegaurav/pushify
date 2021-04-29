# Generated by Django 3.2 on 2021-04-29 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('websites', '0005_alter_website_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcm_token', models.TextField()),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='notification_icons')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='notification_banner')),
                ('launch_url', models.URLField(blank=True, max_length=500, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_cb', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_ub', to=settings.AUTH_USER_MODEL)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websites.website')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ('-created_on',),
            },
        ),
    ]
