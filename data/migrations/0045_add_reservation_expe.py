# Generated by Django 3.2.11 on 2022-01-27 13:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0044_merge_0041_blog_tags_0043_auto_20220120_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='canteen',
            name='reservation_expe_participant',
            field=models.BooleanField(blank=True, null=True, verbose_name="participnte à l'expérimentation réservation"),
        ),
        migrations.CreateModel(
            name='ReservationExpe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('experimentation_start_date', models.DateField(blank=True, null=True, verbose_name="date de début d'expérimentation")),
                ('reservation_system_start_date', models.DateField(blank=True, null=True, verbose_name='date de début du système de réservation')),
                ('reservation_system_description', models.TextField(blank=True, null=True, verbose_name='description du système de réservation')),
                ('publicise_method', models.TextField(blank=True, null=True, verbose_name='méthode de communication aux convives')),
                ('leader_first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="prénom du chef d'expé")),
                ('leader_last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="nom du chef d'expé")),
                ('leader_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email du responsable')),
                ('has_regulations', models.BooleanField(default=False, verbose_name='Un réglement à destination des convives a été rédigé')),
                ('has_committee', models.BooleanField(default=False, verbose_name='Un comité de pilotage du projet a été défini')),
                ('avg_weight_not_served_t0', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des excédents présentés aux convives et non servis (g/ convive) sur 20 déjeuners successifs')),
                ('avg_weight_leftover_t0', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des restes des assiettes exprimées (g/convive) sur 20 déjeuners successifs')),
                ('ratio_edible_non_edible_t0', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Ratio de la part non comestible (g) rapportée à la part comestible (g)')),
                ('avg_weight_preparation_leftover_t0', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des excédents de préparation (g/convive)')),
                ('avg_weight_bread_leftover_t0', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des pains jetés sur 20 déjeuners successifs (g/convive)')),
                ('avg_attendance_count_t0', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Taux de fréquentation moyen')),
                ('solution_use_rate_t0', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Taux d’utilisation de la solution de réservation')),
                ('satisfaction_t0', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Satisfaction')),
                ('comments_t0', models.TextField(blank=True, null=True, verbose_name='Commentaires')),
                ('avg_weight_not_served_t1', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des excédents présentés aux convives et non servis (g/ convive) sur 20 déjeuners successifs')),
                ('avg_weight_leftover_t1', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des restes des assiettes exprimées (g/convive) sur 20 déjeuners successifs')),
                ('ratio_edible_non_edible_t1', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Ratio de la part non comestible (g) rapportée à la part comestible (g)')),
                ('avg_weight_preparation_leftover_t1', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des excédents de préparation (g/convive)')),
                ('avg_weight_bread_leftover_t1', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des pains jetés sur 20 déjeuners successifs (g/convive)')),
                ('avg_attendance_count_t1', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Taux de fréquentation moyen')),
                ('solution_use_rate_t1', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Taux d’utilisation de la solution de réservation')),
                ('satisfaction_t1', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Satisfaction')),
                ('comments_t1', models.TextField(blank=True, null=True, verbose_name='Commentaires')),
                ('avg_weight_not_served_t2', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des excédents présentés aux convives et non servis (g/ convive) sur 20 déjeuners successifs')),
                ('avg_weight_leftover_t2', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des restes des assiettes exprimées (g/convive) sur 20 déjeuners successifs')),
                ('ratio_edible_non_edible_t2', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Ratio de la part non comestible (g) rapportée à la part comestible (g)')),
                ('avg_weight_preparation_leftover_t2', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des excédents de préparation (g/convive)')),
                ('avg_weight_bread_leftover_t2', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Moyenne des pesées des pains jetés sur 20 déjeuners successifs (g/convive)')),
                ('avg_attendance_count_t2', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Taux de fréquentation moyen')),
                ('solution_use_rate_t2', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Taux d’utilisation de la solution de réservation')),
                ('satisfaction_t2', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Satisfaction')),
                ('comments_t2', models.TextField(blank=True, null=True, verbose_name='Commentaires')),
                ('system_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Coût de la solution de réservation sur 3 ans')),
                ('participation_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Coûts liés à la participation à l'expérimentation sur 3 ans")),
                ('participation_cost_details', models.TextField(blank=True, null=True, verbose_name="Détails des coûts liés à la participation à l'expérimentation")),
                ('money_saved', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Gains générés par l'évitement du gaspillage laimentaire en euros sur 3 ans")),
                ('canteen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.canteen', verbose_name='cantine')),
            ],
            options={
                'verbose_name': 'expérimentation réservation',
                'verbose_name_plural': 'expérimentations réservation',
            },
        ),
    ]
