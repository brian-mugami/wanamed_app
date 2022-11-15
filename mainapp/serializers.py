from rest_framework import serializers
from .models import  PatientsModel, DepartmentsModel, ServicesModel 

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    usertype = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    phone_number = serializers.CharField()
    department = serializers.CharField()
    date_joined = serializers.CharField(read_only=True)
    last_login = serializers.CharField(read_only=True)
    username = serializers.CharField()
        
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