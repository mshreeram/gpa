# Generated by Django 4.2 on 2023-05-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_profile_eightsem_profile_fifthsem_profile_firstsem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='eightSem',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fifthSem',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstSem',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fourthSem',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='secondSem',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='seventhSem',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sixthSem',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='thirdSem',
            field=models.FloatField(default=0),
        ),
    ]
