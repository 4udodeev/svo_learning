# Generated by Django 5.0.4 on 2024-04-18 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_center', '0001_initial'),
        ('users', '0005_rename_middlename_employee_middle_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseposition',
            name='training_requirements',
            field=models.ManyToManyField(blank=True, related_name='base_positions', to='training_center.educationmethod', verbose_name='Обязательное обучение'),
        ),
    ]
