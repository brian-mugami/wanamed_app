from django.contrib import admin
from .models import UsersModel, DepartmentsModel, ServicesModel, PatientsModel, AppointmentModel
# Register your models here.
@admin.register(DepartmentsModel)
class DeptAdmin(admin.ModelAdmin):
    ordering = ('department',) 
    search_fields = ('department',)
    
@admin.register(UsersModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'department', 'username', 'email', 'is_staff') 
    ordering = ('first_name',) 
    search_fields = ('name',"department")

@admin.register(AppointmentModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('patient', 'department', 'doctor', 'date', 'description', "seen") 
    ordering = ('date',) 
    search_fields = ('patient_id',"department")