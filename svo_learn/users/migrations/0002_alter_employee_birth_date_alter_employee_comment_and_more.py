# Generated by Django 5.0.4 on 2024-04-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', 'мужской'), ('female', 'женский')], max_length=15, null=True, verbose_name='Пол'),
        ),
    ]
