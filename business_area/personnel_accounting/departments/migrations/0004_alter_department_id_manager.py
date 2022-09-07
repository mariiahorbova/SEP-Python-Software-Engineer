# Generated by Django 4.1.1 on 2022-09-06 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("workers", "0002_alter_worker_id_position"),
        ("departments", "0003_department_workers_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="id_manager",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="workers.worker",
            ),
        ),
    ]