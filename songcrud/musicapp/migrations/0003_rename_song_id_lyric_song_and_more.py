# Generated by Django 4.1.2 on 2022-10-26 02:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_alter_lyric_song_id_alter_song_artiste_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='song_id',
            new_name='song',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='artiste_id',
            new_name='artiste',
        ),
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]