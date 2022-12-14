from rest_framework.response import Response
from .auth import UserAuth
from rest_framework import views, status, permissions, viewsets
from .models import AppointmentModel
from .serializers import AppointmentSerilizer

class AppointmentView(viewsets.ViewSet):
    authentication_classes = (UserAuth,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def list(self, request):
        user = request.user
        if user.usertype == "RECEPTIONIST" or user.is_superuser==True:
            appointments = AppointmentModel.objects.all()
            serializer = AppointmentSerilizer(data=appointments, many=True)
            serializer.is_valid()  
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
    def create(self, request):
        user = request.user
        if user.usertype == "RECEPTIONIST":
            serializer = AppointmentSerilizer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            serializer.save()
            return Response(data={"message": "assigned"}, status=status.HTTP_201_CREATED)