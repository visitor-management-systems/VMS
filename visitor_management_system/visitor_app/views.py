from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from visitor_app.forms import VisitorRegistrationForm,VisitorLogoutForm
from .models import Visitor, VisitorLog, Category, Department, Staff, Enterprise, PostalService
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import PostalService  # Import the PostalService model



import sys
print(sys.path)

    

def visitorlogout_poojitha(request):
    
    # Implement logic for displaying all data
    return render(request, 'visitorlogout.html')
def smday(request):
    return render(request, 'smday.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to alldata.html after successful login
            return redirect('visitor_app:all_data')
        else:
            # Authentication failed
            # Add your logic to handle authentication failure, such as displaying an error message
            pass
    return render(request, 'login.html')

def all_data(request):
    
    # Implement logic for displaying all data
    return render(request, 'alldata.html')


def anusha(request):
    
    # Implement logic for displaying all data
    return render(request, 'exisitingvisitor.html')


def barcode(request):
    # Implement barcode-related logic
    return render(request, 'barcode.html')



def category(request):
    # Implement logic for managing categories
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def department(request):
    # Implement logic for managing departments
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})

def enterprise(request):
    # Implement logic for managing enterprise details
    enterprise_details = Enterprise.objects.all()
    return render(request, 'enterprise1.html', {'enterprise_details': enterprise_details})

def postal_service(request):
    # Retrieve postal entries from the database
    postal_entries = PostalService.objects.all()

    # Pass postal_entries to the template context
    return render(request, 'postal.html', {'postal_entries': postal_entries})

def reports(request):
    # Implement logic for generating reports
    return render(request, 'Reports.html')

def staff_master(request):
    # Implement logic for managing staff details
    staff_members = Staff.objects.all()
    return render(request, 'staffmaster.html', {'staff_members': staff_members})

def run(request):
    return render(request, 'multiple.html')

def multilogin(request):
    return render(request, 'multilogin.html')


def user_master(request):
    # Implement logic for managing user accounts
    # For example:
    users = User.objects.all()
    return render(request, 'usermaster.html', {'users': users})
def visitor_registration(request):
    # Implement logic for visitor registration
    if request.method == 'POST':
        form = VisitorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record inserted successfully!')
            return redirect('visitor_registration')
        else:
            messages.error(request, 'Error in form submission. Please check your input.')
    else:
        form = VisitorRegistrationForm()
    
    return render(request, 'visitorregistration.html', {'form': form})

def visitor_logout(request):
    # Implement logic for visitor logout
    if request.method == 'POST':
        form = VisitorLogoutForm(request.POST)
        if form.is_valid():
            # Handle visitor logout
            # ...
            messages.success(request, 'User logged out successfully!')
            return redirect('visitor_logout')
        else:
            messages.error(request, 'Error in form submission. Please check your input.')
    else:
        form = VisitorLogoutForm()

    return render(request, 'visitorlogout.html', {'form': form})


