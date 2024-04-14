# Generated by Django 4.2.10 on 2024-04-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_board_enpassant'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.CharField(choices=[(None, 'None'), ('w', 'white'), ('b', 'black'), ('d', 'draw')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='turn',
            field=models.CharField(choices=[('w', 'white'), ('b', 'black')], max_length=1),
        ),
    ]
