# Generated by Django 4.1.1 on 2022-09-07 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vacations", "0002_alter_vacation_id_worker"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vacation",
            old_name="id_worker",
            new_name="worker",
        ),
    ]