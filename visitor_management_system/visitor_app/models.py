


from django.db import models
from django.contrib.auth.models import User

class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    tel_no = models.CharField(max_length=15)
    fax_no = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Staff(models.Model):
    name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15)
    tel_no = models.CharField(max_length=15)
    extn = models.CharField(max_length=10)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Security', 'Security'),
    ]
    role = models.CharField(max_length=10, choices=role_choices)

class PostalService(models.Model):
    type = models.CharField(max_length=50)
    reg_date_time = models.DateTimeField()
    from_address = models.TextField()
    to_address = models.TextField()
    through = models.CharField(max_length=50)
    ref_number = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)

class Visitor(models.Model):
    pass_type_choices = [
        ('Single Day', 'Single Day'),
        ('Multiple Days', 'Multiple Days'),
    ]
    pass_type = models.CharField(max_length=20, choices=pass_type_choices)
    valid_day = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    visitor_name = models.CharField(max_length=100)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    company_name = models.CharField(max_length=100)
    address = models.TextField()
    in_date_time = models.DateTimeField()
    purpose = models.CharField(max_length=255)

class VisitorLog(models.Model):
    barcode_no = models.CharField(max_length=50)

    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=20)
    item_carried = models.CharField(max_length=255)
    item_issued = models.CharField(max_length=255)
    badge_no = models.CharField(max_length=20)
    item_deposited = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)

# Add more models as per your requirements
