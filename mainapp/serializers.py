from rest_framework import serializers
from .models import UsersModel, PatientsModel, DepartmentsModel, ServicesModel

class UserSerializer(serializers.Serializer):
    class Meta:
        model = UsersModel
        fields = "__all__"
        
class PatientSerializer(serializers.Serializer):
    class Meta:
        model = PatientsModel
        fields = "__all__"
        
class DepartmentSerializer(serializers.Serializer):
    class Meta:
        model = DepartmentsModel
        fields = "__all__"
        
class ServiceSerializer(serializers.Serializer):
    class Meta:
        model = ServicesModel
        fields = "__all__"