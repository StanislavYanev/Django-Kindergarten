# Generated by Django 5.0.6 on 2024-07-01 05:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_teacher_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='experience',
            field=models.DecimalField(decimal_places=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0.0, message='Value must be positive.')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='short_description',
            field=models.TextField(),
        ),
    ]
