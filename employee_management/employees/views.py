from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Department, Position, Employee, User
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer, UserSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse


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
            'register': '/api/register/',
            'login': '/api/login/',
            'departments': '/api/departments/',
            'positions': '/api/positions/',
            'employees': '/api/employees/',
        })

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"id": user.id, "username": user.username, "email": user.email}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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