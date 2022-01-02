# Generated by Django 2.0.2 on 2022-01-01 14:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_notes_notestype'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='auth_token',
            field=models.CharField(default=datetime.datetime(2022, 1, 1, 14, 28, 50, 311483, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 1, 1, 14, 29, 3, 867767, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]