# Generated by Django 5.0.6 on 2024-07-12 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_games',
            field=models.ManyToManyField(to='admin_panel.childrengames'),
        ),
    ]
