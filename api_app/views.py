
from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from app_main.models import Employee
from .serializers import EmployeeSerializer
class EmployeeViewSet(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
