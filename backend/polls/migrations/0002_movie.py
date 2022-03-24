# Generated by Django 4.0.3 on 2022-03-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('oth_title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('rating_num', models.IntegerField(default=0)),
                ('picture', models.CharField(max_length=200)),
            ],
        ),
    ]
