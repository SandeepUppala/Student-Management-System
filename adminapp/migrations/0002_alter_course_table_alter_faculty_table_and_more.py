# Generated by Django 4.2.9 on 2024-01-20 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='course',
            table='Course_table',
        ),
        migrations.AlterModelTable(
            name='faculty',
            table='Faculty_table',
        ),
        migrations.AlterModelTable(
            name='student',
            table='Student_Table',
        ),
    ]
