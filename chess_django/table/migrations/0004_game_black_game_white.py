# Generated by Django 4.2.10 on 2024-04-20 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('table', '0003_game_winner_alter_board_turn'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='black',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='black_games', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='white',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='white_games', to=settings.AUTH_USER_MODEL),
        ),
    ]
