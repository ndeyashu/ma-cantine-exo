# Generated by Django 5.0.7 on 2024-09-09 16:22

import os
import ckeditor.fields
import data.fields
import django.db.models.deletion
from django.db import migrations, models
from django.core.serializers import deserialize


def restore_waste_action_data(apps, schema_editor):
    try:
        with open("waste_action_backup.json", "r") as f:
            data = f.read()
        data = data.replace("cms.wasteaction", "data.wasteaction")
        for obj in deserialize("json", data):
            obj.save()
        os.remove("waste_action_backup.json")
    except:  # noqa
        pass


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0151_merge_20240906_1852"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="WasteAction",
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
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date de création"
                    ),
                ),
                (
                    "modification_date",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Date de dernière modification"
                    ),
                ),
                ("title", models.TextField(verbose_name="Titre")),
                (
                    "subtitle",
                    models.TextField(blank=True, null=True, verbose_name="Sous-titre"),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        default="<h2>Description</h2><h2>Conseils pratiques</h2><ul><li></li></ul>",
                        verbose_name="Description",
                    ),
                ),
                (
                    "effort",
                    models.CharField(
                        choices=[
                            ("SMALL", "Petit pas"),
                            ("MEDIUM", "Moyen"),
                            ("LARGE", "Grand projet"),
                        ],
                        max_length=255,
                        verbose_name="Niveau d'effort",
                    ),
                ),
                (
                    "waste_origins",
                    data.fields.ChoiceArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("PREP", "Préparation"),
                                ("UNSERVED", "Non servi"),
                                ("PLATE", "Retour assiette"),
                            ],
                            max_length=255,
                        ),
                        size=None,
                        verbose_name="Origines du gaspillage",
                    ),
                ),
                (
                    "lead_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Action anti-gaspi",
                "verbose_name_plural": "Actions anti-gaspi",
                "ordering": ["-modification_date"],
            },
        ),
        migrations.RunPython(restore_waste_action_data),
    ]
