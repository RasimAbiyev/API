from django.urls import reverse
from .permissions import IsAdminOrReadOnly
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Department, Position, Employee, User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer, UserSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrReadOnly]


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAdminOrReadOnly]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnly]


class ApiRootView(generics.GenericAPIView):
    def get(self, request, format=None):
        return Response({
            'register': reverse('register'),
            'login': reverse('login'),
            'departments': reverse('department-list'),
            'positions': reverse('position-list'),
            'employees': reverse('employee-list'),
        })


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data['password'])
        user.save()
        return Response({"id": user.id, "username": user.username, "email": user.email}, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_root(request):
    return Response({
        "departments": request.build_absolute_uri(reverse('department-list')),
        "positions": request.build_absolute_uri(reverse('position-list')),
        "employees": request.build_absolute_uri(reverse('employee-list')),
    })