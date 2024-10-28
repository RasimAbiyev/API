# employees/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, DepartmentViewSet, PositionViewSet, EmployeeViewSet, api_root

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'positions', PositionViewSet, basename='position')
router.register(r'employees', EmployeeViewSet, basename='employee')

# employees/urls.py

from django.urls import path
from .views import RegisterView, LoginView, DepartmentViewSet, PositionViewSet, EmployeeViewSet

from django.urls import path
from .views import RegisterView, LoginView, ApiRootView, DepartmentViewSet, PositionViewSet, EmployeeViewSet

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),  # Add this line for the root view
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('departments/', DepartmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='department-list'),
    path('departments/<int:pk>/', DepartmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='department-detail'),
    path('positions/', PositionViewSet.as_view({'get': 'list', 'post': 'create'}), name='position-list'),
    path('positions/<int:pk>/', PositionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='position-detail'),
    path('employees/', EmployeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='employee-list'),
    path('employees/<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='employee-detail'),
]