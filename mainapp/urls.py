from django.urls import path
from .views import DepartmentsView, ServicesView
from .users import UsersView, LoginView, AuthAPI, LogoutApi

urlpatterns = [
    path("register", UsersView.as_view(), name="register"),
    path("register/<str:pk>", UsersView.as_view(), name="register_id"),
    path("login", LoginView.as_view(), name="login"),
    path("auth", AuthAPI.as_view(), name="auth"),
    path("logout", LogoutApi.as_view(), name="loögout")
        ,
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
]