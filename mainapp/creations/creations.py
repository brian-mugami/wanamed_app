from ..models import LabModel,NurseModel, DoctorModel, OrthopedModel, XrayModel
from ..serializers import LabSerializer
import datetime

def create_lab(patient,assigned_to, description=None, date=datetime.datetime.utcnow()):
    in_lab = LabModel(patient=patient, assigned_to=assigned_to, description=description, upload=None, date=datetime.datetime.utcnow())
    in_lab.save()
    
def create_nurse(patient,assigned_to, description=None, date=datetime.datetime.utcnow()):
    in_nurse = NurseModel(patient=patient, assigned_to=assigned_to, description=description, date=date)
    in_nurse.save()

def create_doctor(patient,assigned_to, description=None, date=datetime.datetime.utcnow()):
    in_doctor = DoctorModel(patient=patient, assigned_to=assigned_to, description=description, date=date)
    in_doctor.save()

def create_orthoped(patient,assigned_to, description=None, date=datetime.datetime.utcnow()):
    in_orthoped = OrthopedModel(patient=patient, assigned_to=assigned_to, description=description, date=date)
    in_orthoped.save()
    
def create_xray(patient,assigned_to, description=None, date=datetime.datetime.utcnow()):
    in_xray = XrayModel(patient=patient, assigned_to=assigned_to, description=description, date=date)
    in_xray.save()