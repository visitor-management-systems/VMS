from django import forms
from .models import Enterprise, Category, Department, Staff, UserProfile, PostalService, Visitor, VisitorLog

class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class PostalServiceForm(forms.ModelForm):
    class Meta:
        model = PostalService
        fields = '__all__'

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'

class VisitorLogForm(forms.ModelForm):
    class Meta:
        model = VisitorLog
        fields = '__all__'
class VisitorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'

class VisitorLogoutForm(forms.ModelForm):
    class Meta:
        model = VisitorLog
        fields = ['barcode_no']  #