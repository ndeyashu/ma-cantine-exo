# Generated by Django 4.2.10 on 2024-03-06 09:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0138_importerror"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ImportError",
            new_name="ImportFailure",
        ),
        migrations.AlterModelOptions(
            name="importfailure",
            options={
                "verbose_name": "échec d'import de masse",
                "verbose_name_plural": "échec d'import de masse",
            },
        ),
    ]
