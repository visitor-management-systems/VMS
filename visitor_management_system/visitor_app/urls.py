from django.urls import path
from . import views

app_name = 'visitor_app'

urlpatterns = [
    path('smday/', views.smday, name='smday'),
    path('login/', views.login, name='login'),
    path('visitorlogout_poojitha/', views.visitorlogout_poojitha, name='visitorlogout_poojitha'),
    path('run/', views.run, name='run'),
    path('anusha/', views.anusha, name='anusha'),

    path('multilogin/', views.multilogin,name='multilogin'),

    path('all_data/', views.all_data, name='all_data'),
    path('barcode/', views.barcode, name='barcode'),
    path('category/', views.category, name='category'),
    path('department/', views.department, name='department'),
    path('enterprise/', views.enterprise, name='enterprise'),
    path('postal_service/', views.postal_service, name='postal_service'),
    path('reports/', views.reports, name='reports'),
    path('staff_master/', views.staff_master, name='staff_master'),
    path('user_master/', views.user_master, name='user_master'),
    path('visitor_registration/', views.visitor_registration, name='visitor_registration'),
    path('visitor_logout/', views.visitor_logout, name='visitor_logout'),
    
    # Add more paths for other views as needed
]
