# Generated by Django 4.0.3 on 2022-03-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating_num',
            field=models.FloatField(default=0),
        ),
    ]
