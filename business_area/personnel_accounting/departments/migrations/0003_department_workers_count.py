# Generated by Django 4.1.1 on 2022-09-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("departments", "0002_remove_department_workers_count_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="workers_count",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
