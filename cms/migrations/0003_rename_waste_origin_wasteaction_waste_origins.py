# Generated by Django 5.0.7 on 2024-08-12 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0002_alter_wasteaction_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wasteaction",
            old_name="waste_origin",
            new_name="waste_origins",
        ),
    ]
