from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import UsersModel,PatientsModel,ServicesModel,DepartmentsModel
from .serializers import UserSerializer
# Create your views here.

class UsersView(viewsets.ViewSet):
    def list(self, request):
        users = UsersModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def create(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid(raise_exception=True):
            user.save()
            return Response(data=user.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "Bad request"})
    
    def retrieve(self, request, pk=None):
        user = UsersModel.objects.get(id=pk)
        serializer = UserSerializer(user)
        if not user:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "User not found"})
        
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None):
        user = UsersModel.objects.get(id=pk)
        if not user:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "User not found"})
        
        return Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "User deleted"})
                        
    def update(self, request, pk=None):
        user = UsersModel.objects.get(id=pk)
        if not user:
            return Response({"message": "user not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
            
        
        