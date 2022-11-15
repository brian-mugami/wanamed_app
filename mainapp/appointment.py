from rest_framework.response import Response
from django.http import HttpResponse
from .auth import UserAuth
from rest_framework import views, status, permissions
from .models import AppointmentModel,PatientsModel, DepartmentsModel, UsersModel
from .serializers import AppointmentSerializer

class AppointmentView(views.APIView):
    authentication_classes = (UserAuth,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        user = request.user
        if user.usertype == "RECEPTIONIST" or user.usertype == "PHYSCICIAN" or user.usertype == "ORTHOPEDIC DOCTOR" :
            appointments = AppointmentModel.objects.all()
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def post(self, request):
        user = request.user
        if user.usertype == "RECEPTIONIST":
            serializer = AppointmentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            
            dept = DepartmentsModel.objects.filter(id=data["department"]).first()
            pat = PatientsModel.objects.get(id=data["patient"])
            doc = UsersModel.objects.get(id=data["doctor"])
            appointment = AppointmentModel(patient=pat, department=dept, doctor=doc, date=data["date"], description=data["description"])
            
            appointment.save()
            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        
    def retrieve(self, request, pk=None):
        user = request.user
        if user.usertype == "RECEPTIONIST" or user.usertype == "PHYSCICIAN" or user.usertype == "ORTHOPEDIC DOCTOR" :
            appointment = AppointmentModel.objects.get(id=pk)
            if not appointment:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "appointment not found"})
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    
    def delete(self, request, pk=None):
        user = request.user
        appointment = AppointmentModel.objects.get(id=pk)
        if  user.usertype == "PHYSCICIAN" or user.usertype == "ORTHOPEDIC DOCTOR":
            if not appointment:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "appointment not found"})
            appointment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "appointment deleted"})
        return Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "cannot appointment deleted"})
                        
    def put(self, request, pk=None):
        user = request.user
        if user.usertype == "RECEPTIONIST":
            appointment = AppointmentModel.objects.get(id=pk)
            if appointment is None:
                return Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "appointment not found"})
            serializer = AppointmentSerializer(instance=appointment, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)