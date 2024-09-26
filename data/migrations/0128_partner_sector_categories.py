# Generated by Django 4.2.4 on 2023-09-04 12:35

import data.fields
from django.db import migrations, models

def populate_sector_categories(apps, schema_editor):
    Partner = apps.get_model('data', 'Partner')
    for partner in Partner.objects.all():
        partner.sector_categories = list(set([sector.category for sector in partner.sectors.all() if sector.category is not None]))
        partner.save()


def undo_populate_sector_categories(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0127_merge_20230818_1344"),
    ]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="sector_categories",
            field=data.fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("administration", "Administration"),
                        ("enterprise", "Entreprise"),
                        ("education", "Enseignement"),
                        ("health", "Santé"),
                        ("social", "Social / Médico-social"),
                        ("leisure", "Loisirs"),
                        ("autres", "Autres"),
                    ],
                    max_length=255,
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="Catégorie du secteur dans lequel ce partenaire situe son activité",
            ),
        ),
        migrations.RunPython(populate_sector_categories, undo_populate_sector_categories),
    ]
