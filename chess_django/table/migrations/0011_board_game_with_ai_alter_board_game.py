# Generated by Django 4.2.10 on 2024-08-08 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0010_gamewithai_black_gamewithai_black_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='game_with_ai',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='table.gamewithai'),
        ),
        migrations.AlterField(
            model_name='board',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='table.game'),
        ),
    ]
