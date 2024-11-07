from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, ApiRootView, DepartmentViewSet, PositionViewSet, EmployeeViewSet
from .views import send_notifications

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'positions', PositionViewSet, basename='position')
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),  # Include router URLs
    path('send_notifications/', send_notifications, name='send_notifications'),
]