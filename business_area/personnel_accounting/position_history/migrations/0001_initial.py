# Generated by Django 4.1.1 on 2022-09-05 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("positions", "0001_initial"),
        ("workers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PositionHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField(blank=True)),
                ("end_date", models.DateField(blank=True)),
                (
                    "id_position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="positions.position",
                    ),
                ),
                (
                    "id_worker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="workers.worker"
                    ),
                ),
            ],
            options={
                "verbose_name": "Position history",
                "verbose_name_plural": "Position histories",
            },
        ),
    ]