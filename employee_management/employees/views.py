from django.shortcuts import render

from rest_framework import viewsets
from .models import Department, Position, Employee
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer

# employees/views.py

from rest_framework import viewsets, permissions
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensures only authenticated users can access

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensures only authenticated users can access


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensures only authenticated users can access

from rest_framework.views import APIView
from rest_framework.response import Response

class ApiRootView(APIView):
    def get(self, request, format=None):
        return Response({
            'register': '/api/register/',
            'login': '/api/login/',
            'departments': '/api/departments/',
            'positions': '/api/positions/',
            'employees': '/api/employees/',
        })

from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"id": user.id, "username": user.username, "email": user.email}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer  # Create this serializer

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# employees/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.urls import reverse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_root(request):
    return Response({
        "departments": request.build_absolute_uri(reverse('department-list')),
        "positions": request.build_absolute_uri(reverse('position-list')),
        "employees": request.build_absolute_uri(reverse('employee-list')),
    })