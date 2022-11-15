# Generated by Django 4.1.3 on 2022-11-15 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_alter_usersmodel_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountsmodel',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='appointmentmodel',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='doctormodel',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='labmodel',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='minilabmodel',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='receptionmodel',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='xraymodel',
            old_name='patient_id',
            new_name='patient',
        ),
    ]
