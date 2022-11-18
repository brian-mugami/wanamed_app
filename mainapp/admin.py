from django.contrib import admin
from .models import UsersModel, DepartmentsModel, ServicesModel, PatientsModel, AppointmentModel, ReceptionModel, NurseModel, XrayModel, LabModel, DoctorModel, OrthopedModel
# Register your models here.
@admin.register(DepartmentsModel)
class DeptAdmin(admin.ModelAdmin):
    ordering = ('department',) 
    search_fields = ('department',)
    
@admin.register(UsersModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'department', 'username', 'email', 'is_staff', 'is_superuser') 
    ordering = ('first_name',) 
    search_fields = ('name',"department")
    
@admin.register(PatientsModel)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("patient_type", "first_name","sur_name", "patient_no", "gender", "age" ) 
    ordering = ('date',) 
    search_fields = ('patient_type',"date")
    
@admin.register(ServicesModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "charge") 
    ordering = ('name',) 
    search_fields = ("name",)
    
@admin.register(ReceptionModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("patient", "description", "get_services","assigned_to", "get_service_charge", "paid")  
    
    
admin.site.register(NurseModel)
admin.site.register(AppointmentModel)
admin.site.register(XrayModel)
admin.site.register(LabModel)
admin.site.register(DoctorModel)
admin.site.register(OrthopedModel)