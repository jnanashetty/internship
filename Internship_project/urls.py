"""Internship_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Citizen_complaint_processing.views import indexPage,register,adminlogin,userlogin,user_verification,show_user_account,view_status,verify_admin_login,\
    register_user,show_comp_reg_page,logout,register_complaint,change_address,change_city,change_state,change_pin,change_phone,show_change_password_page,\
    change_password,delete_user,admin_view_complaints,admin_view_citizen_details,process_complaints,process_complaints_final,admin_logout_request,\
    show_complaint_deletion_page,complaint_deletion
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',indexPage),
    path('registration/',register),
    path('adminlogin/',adminlogin),
    path('user/',userlogin),
    path('userlogin/',user_verification),
    path('userprofile/',show_user_account),
    path('complaintstatus/',view_status),
    path('adminenter/',verify_admin_login),
    path('submituser/',register_user),
    path('complaintregistration/',show_comp_reg_page),
    path('logoutrequest/',logout),
    path('submitcomplaintdetails/',register_complaint),
    path('changeaddress/',change_address),
    path('changecity/',change_city),
    path('changestate/',change_state),
    path('changepin/',change_pin),
    path('changephone/',change_phone),
    path('changepasswordrequest/',show_change_password_page),
    path('passwordchange/',change_password),
    path('deleteuser/',delete_user),
    path('adminviewcomplaints/',admin_view_complaints),
    path('adminviewcitizens/',admin_view_citizen_details),
    path('adminprocesscomplaints/',process_complaints),
    path('sendforprocessing/',process_complaints_final),
    path('adminlogout/',admin_logout_request),
    path('deletecomplaintpage/',show_complaint_deletion_page),
    path('deletecomplaint/',complaint_deletion)
]
