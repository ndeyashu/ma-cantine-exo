# Generated by Django 4.2.3 on 2023-08-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0122_merge_20230801_1140"),
    ]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="contact_phone_number",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Numéro téléphone"
            ),
        ),
    ]
