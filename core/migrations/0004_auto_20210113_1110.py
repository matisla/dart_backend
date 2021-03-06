# Generated by Django 3.1.5 on 2021-01-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_auto_20210113_1058"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="leg",
            name="max_score",
        ),
        migrations.AddField(
            model_name="game",
            name="max_score",
            field=models.IntegerField(
                choices=[(301, 301), (501, 501), (701, 701)], default=501
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="game",
            name="mode",
            field=models.CharField(
                choices=[
                    ("single", "single out"),
                    ("multi", "mutliple out"),
                    ("double", "double out"),
                ],
                default="single",
                max_length=64,
            ),
            preserve_default=False,
        ),
    ]
