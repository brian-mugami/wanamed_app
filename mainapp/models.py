from django.db import models
from random import randint
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import  AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,first_name: str, last_name:str, email:str,password:str=None, is_staff=True, is_superuser=False, usertype="USER", phone_number="0000"):
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.phone_number = phone_number
        user.usertype = usertype
        user.save()
        
        return user
    
    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(first_name=first_name, last_name=last_name,email=email,password=password ,is_staff=True, is_superuser=True, usertype="ADMIN", phone_number=randint(100000, 500000))     
        user.save()
        return user
        
        
class DepartmentsModel(models.Model):
    department = models.CharField(max_length=50, blank=False, unique=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return  self.department

class UsersModel(AbstractUser):
    class UserTypes(models.TextChoices):
        ORTHOPEDIC_DOCTOR = 'ORTHOPEDIC DOCTOR', _('ORTHOPEDIC DOCTOR')
        PHYSICIAN = "PHYSICIAN", _('PHYSCICIAN')
        LAB_TECH = 'LAB TECH', _('LAB TECH')
        RECEPTIONIST = 'RECEPTIONIST', _('RECEPTIONIST')
        NURSE = 'NURSE', _('NURSE')
        ACCOUNTS = 'ACCOUNTS', _('ACCOUNTS')
        PHARMACIST = "PHARMACIST", _("PHARMACIST")
        INTERN = "INTERN", _("INTERN")
        ADMIN = "ADMIN", _("ADMIN")
        USER = "USER", _("USER")
        
    usertype = models.CharField(max_length=30, choices=UserTypes.choices)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    department = models.ForeignKey(DepartmentsModel, blank=False, on_delete=models.SET_NULL, null=True)
    username = None
    is_staff = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    def __str__(self) -> str:
        return str(self.email)
    
class PatientsModel(models.Model):
    class PatientChoices(models.TextChoices):
        CHILD = "CHILD", _("CHILD")
        ADULT = "ADULT", _("ADULT")
        
    class GenderChoices(models.TextChoices):
        MALE = "MALE", _("MALE")
        FEMALE = "FEMALE", _("FEMALE")
        OTHER ="OTHER", _("OTHER")
        
    patient_type = models.CharField(choices=PatientChoices.choices, max_length=10)
    first_name = models.CharField(blank=False, max_length=50)
    middle_name = models.CharField(max_length=50)
    sur_name = models.CharField(blank=False, max_length=50)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_no = models.CharField(max_length=20, unique=True,blank=True)
    patient_no = models.CharField(max_length=20, unique=True, blank=False)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, default = GenderChoices.OTHER )
    date = models.DateTimeField(default=timezone.now)
    age = models.PositiveIntegerField(blank=False ,default=0)
    
    def __str__(self) -> str:
        return self. first_name + " " + self.sur_name
    
    
class ServicesModel(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    charge = models.PositiveIntegerField(default=1000)

    def __str__(self) -> str:
        return self.name 
    
class AppointmentModel(models.Model):
    patient = models.ForeignKey(PatientsModel,on_delete=models.DO_NOTHING, blank=False)
    department = models.ForeignKey(DepartmentsModel, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    description = models.TextField(blank=True, max_length=100)
    seen = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.patient.first_name} to see {self.department}"
    
class ReceptionModel(models.Model):
    patient = models.ForeignKey(PatientsModel,on_delete=models.CASCADE, blank=False)
    assigned_to = models.ForeignKey(DepartmentsModel, on_delete=models.CASCADE, blank=False)
    services = models.ManyToManyField(ServicesModel)
    description = models.TextField(blank=True,max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(default=False)
    
 
    def get_services(self):
        return "\n".join([ p.name for p in self.services.all()])
    

    def get_service_charge(self):
        return "\n".join([ str(p.charge) for p in self.services.all()])

    
    def __str__(self):
        return f"{self.patient} assigned to {self.assigned_to} for {self.services.name}"

class LabModel(models.Model):
    patient = models.ForeignKey(PatientsModel,on_delete=models.CASCADE, blank=False)
    assigned_to = models.ForeignKey(DepartmentsModel, on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=True,max_length=1000)
    upload = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateTimeField()
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.patient.first_name+" "+ self.patient.sur_name+" "+self.patient.middle_name)

class NurseModel(models.Model):
    patient = models.ForeignKey(PatientsModel,on_delete=models.CASCADE, blank=False)
    assigned_to = models.ForeignKey(DepartmentsModel, on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=True,max_length=1000)
    upload = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.patient.first_name+" "+ self.patient.sur_name+" "+self.patient.middle_name)
    
class XrayModel(models.Model):
    patient = models.ForeignKey(PatientsModel,on_delete=models.CASCADE, blank=False)
    assigned_to = models.ForeignKey(DepartmentsModel, on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=True,max_length=500)
    upload = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.patient.first_name+" "+ self.patient.sur_name+" "+self.patient.middle_name)
    
class DoctorModel(models.Model):
    patient = models.ForeignKey(PatientsModel,on_delete=models.CASCADE, blank=False)
    assigned_to = models.ForeignKey(DepartmentsModel, on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=True,max_length=1000)
    prescription = models.TextField(blank=True,max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.patient.first_name+" "+ self.patient.sur_name+" "+self.patient.middle_name)
    
class OrthopedModel(models.Model):
    patient = models.ForeignKey(PatientsModel,on_delete=models.CASCADE, blank=False)
    assigned_to = models.ForeignKey(DepartmentsModel, on_delete=models.CASCADE, blank=False)
    description = models.TextField(blank=True,max_length=1000)
    prescription = models.TextField(blank=True,max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)
    def __str__(self):
        return str(self.patient.first_name+" "+ self.patient.sur_name+" "+self.patient.middle_name)
    

     
    
