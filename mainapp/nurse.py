from rest_framework.response import Response
from .auth import UserAuth
from rest_framework import status, permissions, viewsets
from .models import NurseModel
from .serializers import NurseSerializer

class NurseView(viewsets.ViewSet):
    authentication_classes = (UserAuth,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def list(self, request):
        user = request.user
        if user.usertype == "LAB_TECH" or user.is_superuser==True:
            lab = NurseModel.objects.all()
            serializer = NurseSerializer(data=lab, many=True)
            serializer.is_valid()  
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data={"Message": "Unauthorized"})
        
    def create(self, request):
        user = request.user
        if user.usertype == "LAB_TECH":
            serializer = NurseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data={"message": "assigned"}, status=status.HTTP_201_CREATED)
            
            