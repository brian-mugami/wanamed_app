from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from .auth import UserAuth
from .models import PatientsModel
from .serializers import PatientSerializer

class PatientsView(viewsets.ViewSet):
    authentication_classes = (UserAuth,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def create(self, request):
        user = request.user
        if user.usertype == "RECEPTIONIST":
            patient = PatientSerializer(data=request.data)
            if patient.is_valid(raise_exception=True):
                patient.save()
                return Response(data = patient.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_204_NO_CONTENT, data={"message":"patient not created!!"})
    
    def list(self, request):
        user = request.user
        if user.usertype == "RECEPTIONIST":
            patients = PatientsModel.objects.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def retrieve(self, request, pk=None):
        user = request.user
        if user.usertype == "RECEPTIONIST":
            patient = PatientsModel.objects.get(id=pk)
            if patient is None:
                return Response(status=status.HTTP_204_NO_CONTENT, data={"message":"patient not available!!"})
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None):
        patient = PatientsModel.objects.get(id=pk)
        if not patient:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "Patient not found"})
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "Patient deleted"})
                        
    def update(self, request, pk=None):
        user = request.user
        if user.usertype == "RECEPTIONIST":
            patient = PatientsModel.objects.get(id=pk)
            if patient is None:
                return {"message": "dept not found"}
            serializer = PatientSerializer(instance=patient, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)