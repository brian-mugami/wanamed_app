# Generated by Django 4.1.3 on 2022-11-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_usersmodel_managers_appointmentmodel_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentsmodel',
            name='department',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]