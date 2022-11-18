from rest_framework.response import Response
from .auth import UserAuth
from rest_framework import status, permissions, viewsets
from .models import LabModel
from .serializers import LabSerializer

class MinilabView(viewsets.ViewSet):
    authentication_classes = (UserAuth,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def list(self, request):
        user = request.user
        if user.usertype == "LAB_TECH" or user.is_superuser==True:
            lab = LabModel.objects.all()
            serializer = LabSerializer(data=lab, many=True)
            serializer.is_valid()  
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data={"Message": "Unauthorized"})
        
    def create(self, request):
        user = request.user
        if user.usertype == "LAB_TECH":
            serializer = LabSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data={"message": "assigned"}, status=status.HTTP_201_CREATED)