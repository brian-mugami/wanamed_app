from rest_framework.response import Response
import datetime
from .auth import UserAuth
from rest_framework import views, status, permissions, viewsets
from .models import  LabModel, NurseModel, DepartmentsModel, ReceptionModel
from .serializers import ReceptionSerilizer
from .creations.creations import create_lab, create_xray,create_nurse,create_doctor,create_orthoped

class ReceptionView(viewsets.ViewSet):
    authentication_classes = (UserAuth,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def list(self, request):
        user = request.user
        if user.usertype == "RECEPTIONIST" or user.is_superuser==True:
            receptions = ReceptionModel.objects.all()
            serializer = ReceptionSerilizer(data=receptions, many=True)
            serializer.is_valid()  
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data={"message": "unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def create(self, request):
        user = request.user
        reception_data = request.data
        if user.usertype == "RECEPTIONIST":
            serializer = ReceptionSerilizer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            serializer.save()
            dept = DepartmentsModel.objects.get(id = reception_data["assigned_to"])
            if dept.department == "Lab":
                create_lab(patient=data["patient"],assigned_to=data["assigned_to"], description=data["description"], date=datetime.datetime.utcnow())
                return Response(data={"message": "assigned to lab"}, status=status.HTTP_201_CREATED)
            if dept.department == "Xray":
                create_xray(patient=data["patient"],assigned_to=data["assigned_to"], description=data["description"], date=datetime.datetime.utcnow())
                return Response(data={"message": "assigned to xray"}, status=status.HTTP_201_CREATED)
            if dept.department == "Doctor":
                create_doctor(patient=data["patient"],assigned_to=data["assigned_to"], description=data["description"], date=datetime.datetime.utcnow())
                return Response(data={"message": "assigned to doctor"}, status=status.HTTP_201_CREATED)
            if dept.department == "Orthoped":
                create_orthoped(patient=data["patient"],assigned_to=data["assigned_to"], description=data["description"], date=datetime.datetime.utcnow())
                return Response(data={"message": "assigned to orthoped"}, status=status.HTTP_201_CREATED)
            if dept.department == "Nurse":
                create_nurse(patient=data["patient"],assigned_to=data["assigned_to"], description=data["description"], date=datetime.datetime.utcnow())
                return Response(data={"message": "assigned to nurse"}, status=status.HTTP_201_CREATED)
                
            return Response(data={"message": "assigned"}, status=status.HTTP_201_CREATED)
        return Response(data={"message": "unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)