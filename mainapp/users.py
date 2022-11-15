from .models import UsersModel
from .models import DepartmentsModel
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status, views, exceptions, permissions
from .auth import UserAuth
from werkzeug.security import check_password_hash,generate_password_hash
from .services import create_token
import datetime

class UsersView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        dept = DepartmentsModel.objects.get(id=data["department"])
        password1 = data["password1"]
        password2 = data["password2"]
        
        if password1 == password2:
           # bytes = password1.encode('utf-8')
           # salt = bcrypt.gensalt()
            password = generate_password_hash(password1, method="pbkdf2:sha256")
            user = UsersModel(first_name=data["first_name"], last_name=data["last_name"], email=data["email"],
                            password = password, phone_number=data["phone_number"], department=dept, usertype=data["usertype"], username=data["username"])
            
            user.save()
            return Response(data=data, status=status.HTTP_201_CREATED)
        
        return  Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "Passwords have to match!!"})
    
    def get(self, request):
        users = UsersModel.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        user = UsersModel.objects.get(id=pk)
        user.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "User deleted"})
    
    def put(self, request, pk=None):
        user = UsersModel.objects.get(id=pk)
        if user is None:
            return {"message": "dept not found"}
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid()
        data = serializer.validated_data
        return Response(data=data, status=status.HTTP_202_ACCEPTED)
    
class LoginView(views.APIView):
    def post(self, request):
        email = request.data["email"]
        userPassword = request.data["password"] 
        #userBytes = userPassword.encode('utf-8')  
        user = UsersModel.objects.filter(email=email).first()
        if user is not None:
            if check_password_hash(user.password, userPassword):
                token = create_token(user.id)
                
                resp = Response()
                resp.set_cookie(key="jwt", value=token, httponly=True)
                
                return resp
            else:
                raise exceptions.AuthenticationFailed("Invalid password")
        else:
            raise exceptions.AuthenticationFailed("Invalid credentials")
            

class AuthAPI(views.APIView):
    authentication_classes = (UserAuth,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        user = request.user
        
        serializer = UserSerializer(user)
        
        return Response(data=serializer.data)
 
 
    
class LogoutApi(views.APIView):
    authentication_classes = (UserAuth,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request):
        user = request.user
        serializer = UserSerializer(instance =user, data={"last_login": datetime.datetime.utcnow()}) 
        serializer.is_valid()
        serializer.validated_data
        resp = Response()
        resp.delete_cookie("jwt")
        resp.data = serializer.data
        
        
        return resp