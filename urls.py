"""healthcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView, ListView
from apph.models import UserregistrationModel, DiseaseModel, MedicineModel

from apph import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name="index.html")),
    path('homepage/',TemplateView.as_view(template_name="index.html")),
    path('userregistration/',TemplateView.as_view(template_name="userregistration.html")),
    path('saveuser/',views.userregistration),
    path('userlogin/',TemplateView.as_view(template_name="userlogin.html")),
    path('checkuser/',views.userlogin),
    path('userhome/',TemplateView.as_view(template_name="userhome.html")),
    path('changeupwd/',TemplateView.as_view(template_name="changeupwd.html")),
    path('changeuserpwd/',views.changeuserpassword),
    path('patientsreport/',ListView.as_view(template_name="viewpatientsreport.html",model=UserregistrationModel)),
    path('backuser/',TemplateView.as_view(template_name="userhome.html")),
    path('diseasesandmedicine/',ListView.as_view(template_name="alldiseasesnmedicinesuser.html",model=MedicineModel)),
    path('adminlogin/',TemplateView.as_view(template_name="adminlogin.html")),
    path('admincheck/',views.adminlogin),
    path('adminhome/',TemplateView.as_view(template_name="welcomeadmin.html")),
    path('adpatientsreport/',ListView.as_view(template_name="viewpatientsreportadmin.html",model=UserregistrationModel)),
    path('backuseradmin/',TemplateView.as_view(template_name="welcomeadmin.html")),
    path('contactus/',TemplateView.as_view(template_name="homecontactus.html")),
    path('adddisease/',TemplateView.as_view(template_name="adminadddisease.html")),
    path('savedisease/',views.adddisease),
    path('modifydiseases/',views.displayDiseases),
    path('updatedisease/',views.updatediseases),
    path('saveupdateddiseases/',views.saveupdateddiseases),
    path('deletedisease/',views.deletedisease),
    path('addmedicine/', TemplateView.as_view(template_name="addmedicine.html")),
    path('savemedicine/',views.addmedicine),
    path('modifymedicine/',views.displaymedicine),
    path('patientsreportmenu/',ListView.as_view(model=UserregistrationModel,template_name="viewpatientsreportmenu.html")),
    path('backusermenu/',TemplateView.as_view(template_name="index.html")),
    path('updatemedicine/',views.updateMedicine),
    path('updatesavemedicine/',views.updatemedicineadmin),
    path('deletemedicineadmin<int:pk>/',views.DeleteMedicineAdmin.as_view()),
    path('addiseasesandmedicines/',ListView.as_view(template_name="alldiseasesnmedicines.html",model=MedicineModel)),
    path('diseasesandmedicinemenu/',views.displayAll),
    path('backdisplaydiseases/',TemplateView.as_view(template_name="userhome.html")),
    path('searchmedicine/',TemplateView.as_view(template_name="searchmedicineuser.html")),
    path('searchmedicineuser/',views.searchMedicine),
    path('adminlogout/',TemplateView.as_view(template_name="index.html")),
    path('userlogout/',TemplateView.as_view(template_name="index.html")),
]
