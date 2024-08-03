from django.db import models

class UserregistrationModel(models.Model):
    firstname=models.CharField(max_length=150)
    lastname=models.CharField(max_length=150)
    age=models.IntegerField()
    gender=models.CharField(max_length=7)
    address=models.CharField(max_length=300)
    username=models.CharField(primary_key=True,max_length=50)
    password=models.CharField(max_length=100)


class AdminModel(models.Model):
    username=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)

class DiseaseModel(models.Model):
    disease_id=models.IntegerField(primary_key=True)
    disease_name=models.CharField(max_length=200)
    symptoms=models.CharField(max_length=500,default=False)

class MedicineModel(models.Model):
    diseasename=models.CharField(max_length=100)
    symptomname=models.CharField(max_length=100)
    medicinename=models.CharField(max_length=200)
    medicinedescription=models.TextField()


