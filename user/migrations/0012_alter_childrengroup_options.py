# Generated by Django 5.0.6 on 2024-07-12 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_childrengroup_options_alter_teacher_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='childrengroup',
            options={'permissions': [('can_view_child_group', 'Can view children group strawberry '), ('can_view_little_rascals_group', 'Can view children group little rascals ')]},
        ),
    ]
