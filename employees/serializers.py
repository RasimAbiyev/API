import re
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Department, Position, Employee, User
from django.contrib.auth.password_validation import validate_password

# serializers.py
from rest_framework import serializers
from django.utils.translation import gettext as _
from .models import Department, Position, Employee, User

class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="name")

    class Meta:
        model = Department
        fields = ['id', 'name']

class PositionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="name")

    class Meta:
        model = Position
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def validate_password(self, value):
        # Additional custom validations on top of `validate_password`
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', value):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', value):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', value):
            raise ValidationError("Password must contain at least one digit.")
        return value

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user