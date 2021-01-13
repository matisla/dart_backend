# Generated by Django 3.1.5 on 2021-01-12 20:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='best_of',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='game',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
