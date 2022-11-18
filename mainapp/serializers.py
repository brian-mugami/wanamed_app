from rest_framework import serializers
from .models import  PatientsModel, DepartmentsModel, ServicesModel, ReceptionModel, UsersModel, AppointmentModel,LabModel,XrayModel,NurseModel

class UserSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=DepartmentsModel.objects.all())
    class Meta:  
        model = UsersModel
        fields = ["usertype", "first_name", "last_name", "email","phone_number","department"] 
        write_only_fields = ["password",]
        read_only_fields = ["last_login", "date_joined", "id", "is_staff", "is_superuser"]
    
class  ReceptionSerilizer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(queryset=ServicesModel.objects.all(),many=True)
    patient = serializers.PrimaryKeyRelatedField(queryset=PatientsModel.objects.all())
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=DepartmentsModel.objects.all())
    class Meta:
        model = ReceptionModel
        fields= ["services", "patient", "assigned_to", "description"]
        read_only_fields=["id","paid"]
        
      
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientsModel
        fields = "__all__"
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentsModel
        fields = "__all__"
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesModel
        fields = "__all__"
        
class NurseSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=PatientsModel.objects.all())
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=DepartmentsModel.objects.all())
    
    class Meta:
        model = NurseModel
        fields = ["patient", "assigned_to", "upload", "description", "seen"]
        read_only_fields = ["id",]

class  AppointmentSerilizer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=PatientsModel.objects.all())
    department = serializers.PrimaryKeyRelatedField(queryset=DepartmentsModel.objects.all())
    
    class Meta:
        model = AppointmentModel
        fields= ["patient", "department", "date", "description"]
        read_only_fields=["id","seen"]
        
class LabSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=PatientsModel.objects.all())
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=DepartmentsModel.objects.all())
    
    class Meta:
        model = LabModel
        fields = ["patient", "assigned_to", "upload", "description", "seen"]
        read_only_fields = ["id",]
        
class XrayLabSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=PatientsModel.objects.all())
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=DepartmentsModel.objects.all())
    
    class Meta:
        model = XrayModel
        fields = ["patient", "assigned_to", "upload", "description", "seen"]
        read_only_fields = ["id",]
        
