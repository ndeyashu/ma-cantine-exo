# Generated by Django 4.1 on 2022-09-14 15:27

import data.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0090_partner_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partner",
            name="categories",
            field=data.fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("appro", "Améliorer ma part de bio / durable"),
                        ("plastic", "Substituer mes plastiques"),
                        ("asso", "Donner à une association"),
                        ("waste", "Diagnostiquer mon gaspillage"),
                        ("training", "Me former ou former mon personnel"),
                        ("hygiene", "Trouver des aides / conseils sanitaires"),
                    ],
                    max_length=255,
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="Besoin(s) comblé(s) par ce partenaire",
            ),
        ),
    ]
