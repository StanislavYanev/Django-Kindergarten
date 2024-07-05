# Generated by Django 5.0.6 on 2024-06-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('parent', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('picture', models.ImageField(upload_to='teacher_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('picture', models.ImageField(upload_to='teacher_pictures')),
                ('phone_number', models.CharField(max_length=100)),
                ('experience', models.DecimalField(decimal_places=2, max_digits=4)),
                ('short_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Childrens_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teachers_in_group', models.ManyToManyField(to='user.teacher')),
            ],
        ),
    ]
