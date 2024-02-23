from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Department, Enterprise, PostalService, Staff, Visitor, VisitorLog
from .forms import VisitorRegistrationForm, VisitorLogoutForm

class VisitorAppTests(TestCase):
    def setUp(self):
        # Set up initial data for testing
        Category.objects.create(name='Test Category')
        Department.objects.create(name='Test Department')
        Enterprise.objects.create(name='Test Enterprise')
        Staff.objects.create(name='Test Staff', department=Department.objects.first())
        PostalService.objects.create(name='Test Postal Service')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_all_data_view(self):
        response = self.client.get(reverse('alldata'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alldata.html')

    def test_barcode_view(self):
        response = self.client.get(reverse('barcode'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'barcode.html')

    def test_category_view(self):
        response = self.client.get(reverse('category'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')
        self.assertQuerysetEqual(response.context['categories'], ['<Category: Test Category>'])

    def test_department_view(self):
        response = self.client.get(reverse('department'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department.html')
        self.assertQuerysetEqual(response.context['departments'], ['<Department: Test Department>'])

    def test_enterprise_view(self):
        response = self.client.get(reverse('enterprise'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'enterprise.html')
        self.assertEqual(response.context['enterprise_details'].name, 'Test Enterprise')

    def test_postal_service_view(self):
        response = self.client.get(reverse('postal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postal.html')
        self.assertQuerysetEqual(response.context['postal_entries'], ['<PostalService: Test Postal Service>'])

    def test_reports_view(self):
        response = self.client.get(reverse('reports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Reports.html')

    def test_staff_master_view(self):
        response = self.client.get(reverse('staffmaster'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staffmaster.html')
        self.assertQuerysetEqual(response.context['staff_members'], ['<Staff: Test Staff>'])

    def test_user_master_view(self):
        # Add your test cases for user_master view if needed
        pass

    def test_visitor_registration_view(self):
        response = self.client.get(reverse('visitor_registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'visitorregistration.html')

        # Test form submission
        form_data = {
            'name': 'Test Visitor',
            'gender': 'Male',
            'company_name': 'Test Company',
            # Add more form data as needed
        }
        response = self.client.post(reverse('visitor_registration'), form_data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after form submission
        self.assertEqual(Visitor.objects.count(), 1)  # Check if a new visitor record is created

    def test_visitor_logout_view(self):
        response = self.client.get(reverse('visitor_logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'visitorlogout.html')

        # Test form submission
        form_data = {
            'barcode_no': '123456',  # Add a valid barcode number
            # Add more form data as needed
        }
        response = self.client.post(reverse('visitor_logout'), form_data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after form submission
        # Add more assertions based on your logout logic

# Add more test cases as needed for other views and functionalities
