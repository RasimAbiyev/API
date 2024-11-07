from django.test import TestCase
from django.urls import reverse
from django.core.mail import send_mail
from unittest.mock import patch
from employees.models import Employee, Department, Position


class EmployeeTestCase(TestCase):
    
    def setUp(self):
        """Set up an employee, a department, and a position for the tests."""
        # Create a Department object first
        self.department = Department.objects.create(name="Engineering")

        # Now create the Position object with the department
        self.position = Position.objects.create(name="Developer", department=self.department)
        
        # Create an employee and assign the department and position
        self.employee = Employee.objects.create(
            name="Rasim",
            surname="Abiyev",
            email="abiyev.rasim@gmail.com",
            department=self.department,
            position=self.position
        )

    def test_employee_creation(self):
        """Test that an employee can be created successfully."""
        employee = Employee.objects.get(name='Rasim')
        self.assertEqual(employee.name, 'Rasim')
        self.assertEqual(employee.surname, 'Abiyev')
        self.assertEqual(employee.email, 'abiyev.rasim@gmail.com')
        self.assertEqual(employee.position.name, 'Developer')
        self.assertEqual(employee.department.name, 'HR')

    def test_employee_url(self):
        """Test the employee details URL."""
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rasim')

    @patch('django.core.mail.send_mail')
    def test_send_notifications(self, mock_send_mail):
        """Test that the send_notifications task sends emails."""
        mock_send_mail.return_value = True
        response = self.client.get(reverse('send_notifications'))
        
        # Ensure that the email sending function was called
        self.assertTrue(mock_send_mail.called)

import pytest
from unittest.mock import patch
from django.urls import reverse
from employees.models import Employee, Department, Position


@pytest.mark.django_db
def test_employee_creation():
    """Test that an employee can be created."""
    # Create a department and position
    department = Department.objects.create(name="HR")
    position = Position.objects.create(name="Developer")
    
    # Create an employee instance
    employee = Employee.objects.create(
        name='Rasim',
        surname='Abiyev',
        email='abiyev.rasim@gmail.com',
        department=department,
        position=position,
        created_at='2024-11-01'
    )
    
    assert employee.name == 'Rasim'
    assert employee.email == 'abiyev.rasim@gmail.com'
    assert employee.position.name == 'Developer'
    assert employee.department.name == 'HR'


@pytest.mark.django_db
def test_send_notifications(client, mocker):
    """Test that the send_notifications task sends emails."""
    mock_send_mail = mocker.patch('django.core.mail.send_mail')
    response = client.get(reverse('send_notifications'))
    
    # Check that the email sending function was called
    mock_send_mail.assert_called_once()