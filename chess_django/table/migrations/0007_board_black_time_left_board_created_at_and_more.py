# Generated by Django 4.2.10 on 2024-06-18 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_game_black_ready_game_white_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='black_time_left',
            field=models.IntegerField(default=900),
        ),
        migrations.AddField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='white_time_left',
            field=models.IntegerField(default=900),
        ),
    ]
