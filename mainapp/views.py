from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import ServicesModel,DepartmentsModel
from .serializers import DepartmentSerializer,ServiceSerializer

# Create your views here.
class ServicesView(viewsets.ViewSet):
    
    def list(self, request):
        services = ServicesModel.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def create(self, request):
        service = ServiceSerializer(data=request.data)
        if service.is_valid(raise_exception=True):
            service.save()
            return Response(data=service.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "Bad request"})

    
    def retrieve(self, request, pk=None):
        service = ServicesModel.objects.get(id=pk)
        if not service:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "dept not found"})
        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    
    def destroy(self, request, pk=None):
        service = ServicesModel.objects.get(id=pk)
        if not service:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "Dept not found"})
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "service deleted"})
                        
    def update(self, request, pk=None):
        service = ServicesModel.objects.get(id=pk)
        if service is None:
            return Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "service not found"})
        serializer = ServiceSerializer(instance=service, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

class DepartmentsView(viewsets.ViewSet):
    
    def list(self, request):
        depts = DepartmentsModel.objects.all()
        serializer = DepartmentSerializer(depts, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def create(self, request):
        department = DepartmentSerializer(data=request.data)
        if department.is_valid(raise_exception=True):
            department.save()
            return Response(data=department.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "Bad request"})

    
    def retrieve(self, request, pk=None):
        dept = DepartmentsModel.objects.get(id=pk)
        if not dept:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "dept not found"})
        serializer = DepartmentSerializer(dept)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    
    def destroy(self, request, pk=None):
        dept = DepartmentsModel.objects.get(id=pk)
        if not dept:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "Dept not found"})
        dept.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "Dept deleted"})
                        
    def update(self, request, pk=None):
        dept = DepartmentsModel.objects.get(id=pk)
        if dept is None:
            return {"message": "dept not found"}
        serializer = DepartmentSerializer(instance=dept, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)




