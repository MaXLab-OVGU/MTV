# Generated by Django 2.2.5 on 2022-04-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0003_auto_20220408_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='duration',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3),
        ),
    ]
