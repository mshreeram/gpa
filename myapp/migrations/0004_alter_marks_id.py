# Generated by Django 4.2 on 2023-04-29 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_marks_factor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marks",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
