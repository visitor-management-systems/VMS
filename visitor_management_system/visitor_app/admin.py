from django.contrib import admin
from .models import Enterprise, Category, Department, Staff, UserProfile, PostalService, Visitor, VisitorLog

class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'pincode', 'tel_no', 'fax_no', 'email', 'website')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'staff_id', 'department', 'mobile_no', 'tel_no', 'extn')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')

class PostalServiceAdmin(admin.ModelAdmin):
    list_display = ('type', 'reg_date_time', 'from_address', 'to_address', 'through', 'ref_number', 'contact_person', 'mobile_no')

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('pass_type', 'valid_day', 'category', 'department', 'staff', 'visitor_name', 'gender', 'company_name', 'address', 'in_date_time', 'purpose')

class VisitorLogAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'mobile_no', 'location', 'vehicle_no', 'item_carried', 'item_issued', 'badge_no', 'item_deposited', 'remark')

# Register your models with the custom admin classes
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(PostalService, PostalServiceAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(VisitorLog, VisitorLogAdmin)
