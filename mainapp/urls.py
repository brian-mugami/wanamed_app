from django.urls import path
from .views import UsersView

urlpatterns = [
    path("user", UsersView.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path("user/<str:pk>", UsersView.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy'
        }
    )),
]