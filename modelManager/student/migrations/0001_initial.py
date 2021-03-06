# Generated by Django 3.1.2 on 2020-11-22 10:23

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
            managers=[
                ('students', django.db.models.manager.Manager()),
            ],
        ),
    ]
