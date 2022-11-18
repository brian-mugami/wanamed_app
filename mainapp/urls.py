from django.urls import path
from .views import DepartmentsView, ServicesView
from .users import UsersView, LoginView, AuthAPI, LogoutApi
from .patients import PatientsView
from .reception import ReceptionView
from .nurse import NurseView
from .appointment import AppointmentView

urlpatterns = [
    path("register", UsersView.as_view(), name="register"),
    path("register/<str:pk>", UsersView.as_view(), name="register_id"),
    path("login", LoginView.as_view(), name="login"),
    path("auth", AuthAPI.as_view(), name="auth"),
    path("logout", LogoutApi.as_view(), name="logout"),
    path("dept", DepartmentsView.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path("dept/<str:pk>", DepartmentsView.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy'
        }
    )),
     path("service", ServicesView.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path("service/<str:pk>", ServicesView.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy'
        }
    )),
         path("patient", PatientsView.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path("patient/<str:pk>", PatientsView.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy'
        }
    )),
     path("reception", ReceptionView.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path("reception/<str:pk>", ReceptionView.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy'
        }
    )),
    path("minilab", NurseView.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path("minilab/<str:pk>", NurseView.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy'
        }
    )),
    path("appointment", AppointmentView.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path("appointment/<str:pk>", AppointmentView.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy'
        }
    )),
]