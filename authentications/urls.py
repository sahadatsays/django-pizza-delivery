
from django.urls import path
from .views import AuthenticationView

urlpatterns = [
    path("", AuthenticationView.as_view()),
]
