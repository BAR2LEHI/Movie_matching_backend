# Generated by Django 5.0 on 2024-01-18 15:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_preferences_genre_alter_preferences_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)], verbose_name='Бюджет'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='content_rating',
            field=models.CharField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Возрастной рейтинг'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='revenue',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8000000000)], verbose_name='Сборы'),
        ),
    ]
