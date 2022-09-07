# Generated by Django 4.1.1 on 2022-09-06 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("workers", "0002_alter_worker_id_position"),
        ("departments", "0004_alter_department_id_manager"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="id_manager",
            field=models.OneToOneField(
                blank=True,
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="workers.worker",
            ),
        ),
    ]