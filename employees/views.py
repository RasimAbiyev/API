from django.urls import reverse
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Department, Position, Employee, User
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer, RegisterSerializer
from rest_framework.response import Response
from django.utils import translation

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticated]

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        user_language = request.headers.get('Accept-Language', 'en')
        translation.activate(user_language)
        response = super().list(request, *args, **kwargs)
        translation.deactivate()
        return response

# Eyni prosesi PositionViewSet üçün də tətbiq edə bilərsiniz


    def get_permissions(self):
        if self.action == 'destroy':
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_root(request):
    return Response({
        "register": request.build_absolute_uri(reverse('register')),
        "login": request.build_absolute_uri(reverse('login')),
        "departments": request.build_absolute_uri(reverse('department-list')),
        "positions": request.build_absolute_uri(reverse('position-list')),
        "employees": request.build_absolute_uri(reverse('employee-list')),
    })


class ApiRootView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'register': reverse('register', request=request),
            'login': reverse('login', request=request),
            'departments': reverse('department-list', request=request),
            'positions': reverse('position-list', request=request),
            'employees': reverse('employee-list', request=request),
        })