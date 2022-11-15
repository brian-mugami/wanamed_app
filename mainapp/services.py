import dataclasses
import datetime
from .models import UsersModel, DepartmentsModel
import jwt
import os

key_secret = os.environ.get("JWT_SECRET")

@dataclasses.dataclass
class UserDataClass:
    usertype: str
    first_name: str
    sur_name : str
    email: str
    phone_number: str
    department: str
    date_started: str=None
    id: int=None
    password: str = None
    
    @classmethod
    def from_instance(cls, user: "UsersModel")->"UserDataClass":
        return cls(
        usertype= user.usertype,
        first_name= user.first_name,
        sur_name = user.sur_name,
        email = user.email,
        phone_number= user.phone_number,
        department= user.department,
        )
        
def create_user(user:"UserDataClass")->"UserDataClass":
    instance = UsersModel(
        usertype = user.usertype,
        first_name = user.first_name,
        sur_name = user.sur_name,
        email= user.email,
        phone_number=user.phone_number,
        department=DepartmentsModel.objects.get(department=user.department) )
    
    if user.password is not None:
        instance.password(user.password)
        
    instance.save()
    
    return UserDataClass.from_instance()

def create_token(user_id:int)->str:
    payload=dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=48)
    )
    token = jwt.encode(payload,key_secret,algorithm="HS256")
    
    return token