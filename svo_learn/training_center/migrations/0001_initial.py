# Generated by Django 5.0.4 on 2024-04-16 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirectionOfTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EducationOrg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RiskLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TermsOfRetraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EducationMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('cost', models.FloatField(blank=True, null=True, verbose_name='Стоимость за человека')),
                ('duration', models.SmallIntegerField(blank=True, null=True, verbose_name='Количество дней обучения')),
                ('direction_of_training', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='training_center.directionoftraining', verbose_name='Направление обучения')),
                ('edeucation_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training_center.educationorg', verbose_name='Учебная организация')),
                ('risk_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='training_center.risklevel', verbose_name='Уровень риска')),
                ('terms_of_retraining', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='training_center.termsofretraining', verbose_name='Сроки переподготовки')),
            ],
            options={
                'verbose_name': 'Учебная программа',
                'verbose_name_plural': 'Учебные программы',
                'default_related_name': 'education_methods',
            },
        ),
    ]
