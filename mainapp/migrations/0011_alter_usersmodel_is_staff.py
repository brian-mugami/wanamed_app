# Generated by Django 4.1.3 on 2022-11-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_departmentsmodel_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]