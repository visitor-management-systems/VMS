# Generated by Django 4.0.3 on 2024-01-31 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=10)),
                ('tel_no', models.CharField(max_length=15)),
                ('fax_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PostalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('reg_date_time', models.DateTimeField()),
                ('from_address', models.TextField()),
                ('to_address', models.TextField()),
                ('through', models.CharField(max_length=50)),
                ('ref_number', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('staff_id', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(max_length=15)),
                ('tel_no', models.CharField(max_length=15)),
                ('extn', models.CharField(max_length=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_type', models.CharField(choices=[('Single Day', 'Single Day'), ('Multiple Days', 'Multiple Days')], max_length=20)),
                ('valid_day', models.IntegerField(blank=True, null=True)),
                ('visitor_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('in_date_time', models.DateTimeField()),
                ('purpose', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_app.category')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_app.department')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='VisitorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=100)),
                ('vehicle_no', models.CharField(max_length=20)),
                ('item_carried', models.CharField(max_length=255)),
                ('item_issued', models.CharField(max_length=255)),
                ('badge_no', models.CharField(max_length=20)),
                ('item_deposited', models.CharField(max_length=255)),
                ('remark', models.CharField(max_length=255)),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor_app.visitor')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('User', 'User'), ('Security', 'Security')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
