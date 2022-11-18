# Generated by Django 4.1.2 on 2022-11-17 12:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_accountsmodel_date_doctormodel_date_labmodel_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NurseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('upload', models.CharField(blank=True, max_length=300)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('seen', models.BooleanField(default=False)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.departmentsmodel')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.patientsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='OrthopedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('prescription', models.TextField(blank=True, max_length=1000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('seen', models.BooleanField(default=False)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.departmentsmodel')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.patientsmodel')),
            ],
        ),
        migrations.RemoveField(
            model_name='minilabmodel',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='minilabmodel',
            name='patient',
        ),
        migrations.AddField(
            model_name='doctormodel',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='labmodel',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='receptionmodel',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='xraymodel',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='labmodel',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.DeleteModel(
            name='AccountsModel',
        ),
        migrations.DeleteModel(
            name='MiniLabModel',
        ),
    ]
