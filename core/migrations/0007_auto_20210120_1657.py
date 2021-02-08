# Generated by Django 3.1.5 on 2021-01-20 17:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20210118_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='users',
            field=models.ManyToManyField(related_name='games', to=settings.AUTH_USER_MODEL),
        ),
    ]
