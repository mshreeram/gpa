# Generated by Django 4.2 on 2023-05-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nosc',
            field=models.FloatField(default=0),
        ),
    ]
