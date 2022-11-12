from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class DepartmentsModel(models.Model):
    #class DepartmentChoices(models.TextChoices):
    #    LAB = 'LAB', _('LAB')
    #    MINI_LAB = 'MINI LAB', _('LAB TECH')
    #    RECEPTION = 'RECEPTION', _('RECEPTION')
    #    X_RAY = 'X-RAY', _('X-RAY')
    #    ORTHOPEDIC_DOCTOR = 'ORTHOPEDIC DOCTOR', _('ORTHOPEDIC DOCTOR')
    #    PHYSICIAN = "PHYSICIAN", _('PHYSCICIAN')
    #    CHECKOUT = "CHECKOUT", _("CHECKOUT")
    #    PHARMACY = "PHARMACY", _("PHARMACY")
    department = models.CharField(max_length=50, blank=False)

class UsersModel(models.Model):
    class UserTypes(models.TextChoices):
        ORTHOPEDIC_DOCTOR = 'ORTHOPEDIC DOCTOR', _('ORTHOPEDIC DOCTOR')
        PHYSICIAN = "PHYSICIAN", _('PHYSCICIAN')
        LAB_TECH = 'LAB TECH', _('LAB TECH')
        RECEPTIONIST = 'RECEPTIONIST', _('RECEPTIONIST')
        NURSE = 'NURSE', _('NURSE')
        ACCOUNTS = 'ACCOUNTS', _('ACCOUNTS')
        PHARMACIST = "PHARMACIST", _("PHARMACIST")
        
    usertype = models.CharField(max_length=30, choices=UserTypes.choices)
    first_name = models.CharField(blank=False, max_length=50)
    sur_name = models.CharField(blank=False, max_length=50)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(blank=False, max_length=200)
    phone_number = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(DepartmentsModel, blank=False, on_delete=models.SET_NULL, null=True)
    date_started = models.DateTimeField(default=timezone.now)
    available = models.BooleanField(default=True)
    
class PatientsModel(models.Model):
    class PatientChoices(models.TextChoices):
        CHILD = "CHILD", _("CHILD")
        ADULT = "ADULT", _("ADULT")
        
    patient_type = models.CharField(choices=PatientChoices.choices, max_length=10)
    first_name = models.CharField(blank=False, max_length=50)
    middle_name = models.CharField(max_length=50)
    sur_name = models.CharField(blank=False, max_length=50)
    guardian_name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20, unique=True, blank=False)
    date = models.DateTimeField(default=timezone.now)
    
class ServicesModel(models.Model):
    name = models.CharField(max_length=50, blank=False)
    charge = models.PositiveIntegerField(default=1000)
    
class ChargesModel(models.Model):
    patient_id = models.ForeignKey(PatientsModel, on_delete=models.CASCADE, blank=False)
    service = models.ManyToManyField(ServicesModel, blank=False)
    deptartment = models.ManyToManyField(DepartmentsModel, blank=False)
    
class PatientDoctorModel(models.Model):
    patient_id = models.ForeignKey(PatientsModel, on_delete=models.CASCADE, blank=False)
    lab_results = models.TextField(blank=True)
    mini_lab_results = models.TextField(blank=True)
    prescription = models.TextField(blank=True)
    prescription_by = models.ForeignKey(UsersModel,blank=False, on_delete=models.SET_NULL, null= True)
    
    class Meta:
        unique_together = ('patient_id', 'prescription_by')
    
