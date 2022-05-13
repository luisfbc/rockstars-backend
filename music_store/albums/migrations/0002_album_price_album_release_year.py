# Generated by Django 4.0.3 on 2022-05-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='album',
            name='release_year',
            field=models.SmallIntegerField(default=0),
        ),
    ]
