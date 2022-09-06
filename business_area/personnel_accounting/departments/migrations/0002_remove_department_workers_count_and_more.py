# Generated by Django 4.1.1 on 2022-09-06 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("workers", "0001_initial"),
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="department",
            name="workers_count",
        ),
        migrations.AlterField(
            model_name="department",
            name="id_manager",
            field=models.OneToOneField(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="workers.worker",
            ),
        ),
    ]
