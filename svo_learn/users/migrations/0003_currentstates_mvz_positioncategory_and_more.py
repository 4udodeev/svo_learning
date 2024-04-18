# Generated by Django 5.0.4 on 2024-04-16 15:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_center', '0001_initial'),
        ('users', '0002_alter_employee_birth_date_alter_employee_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentStates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Состояние сотрудника',
                'verbose_name_plural': 'Состояния сотрудника',
                'default_related_name': 'current_states',
            },
        ),
        migrations.CreateModel(
            name='Mvz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'МВЗ',
                'verbose_name_plural': 'МВЗ',
                'default_related_name': 'MVZ',
            },
        ),
        migrations.CreateModel(
            name='PositionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория должности',
                'verbose_name_plural': 'Категории должности',
                'default_related_name': 'position_cathegorys',
            },
        ),
        migrations.CreateModel(
            name='PositionTypeOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип должности',
                'verbose_name_plural': 'Типы должности',
                'default_related_name': 'position_types_of_work',
            },
        ),
        migrations.AlterModelOptions(
            name='baseposition',
            options={'default_related_name': 'base_positions', 'verbose_name': 'Типовая должность', 'verbose_name_plural': 'Типовые должности'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'default_related_name': 'organizations', 'verbose_name': 'Организация', 'verbose_name_plural': 'Организации'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'default_related_name': 'positions', 'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='subdivision',
            options={'default_related_name': 'subdivisions', 'verbose_name': 'Подразделение', 'verbose_name_plural': 'Подразделения'},
        ),
        migrations.AddField(
            model_name='baseposition',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код'),
        ),
        migrations.AddField(
            model_name='baseposition',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baseposition',
            name='training_requirements',
            field=models.ManyToManyField(related_name='base_positions', to='training_center.educationmethod', verbose_name='Обязательное обучение'),
        ),
        migrations.AddField(
            model_name='organization',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код'),
        ),
        migrations.AddField(
            model_name='organization',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='position',
            name='code',
            field=models.CharField(default=None, max_length=255, verbose_name='Код'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='position',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='position',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='position',
            name='subdivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.subdivision'),
        ),
        migrations.AddField(
            model_name='subdivision',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код'),
        ),
        migrations.AddField(
            model_name='subdivision',
            name='is_disbanded',
            field=models.BooleanField(default=False, verbose_name='Расформировано'),
        ),
        migrations.AddField(
            model_name='subdivision',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subdivision',
            name='organization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='users.organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subdivision',
            name='parent_subdivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='users.subdivision'),
        ),
        migrations.AddField(
            model_name='employee',
            name='current_state',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.currentstates', verbose_name='Текущее состояние'),
        ),
        migrations.AddField(
            model_name='position',
            name='mvz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.mvz'),
        ),
        migrations.AddField(
            model_name='position',
            name='position_cathegory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.positioncategory'),
        ),
        migrations.AddField(
            model_name='position',
            name='position_type_of_work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.positiontypeofwork'),
        ),
    ]
