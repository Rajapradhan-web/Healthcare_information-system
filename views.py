from django.shortcuts import render
from django.views.generic import DeleteView, DetailView
from .models import UserregistrationModel, AdminModel, DiseaseModel, MedicineModel


def userregistration(request):
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    age=request.POST.get("age")
    gender=request.POST.get("gender")
    address=request.POST.get("address")
    username=request.POST.get("uname")
    password=request.POST.get("upass")
    ur=UserregistrationModel(firstname=fname,lastname=lname,
                             age=age,gender=gender,address=address,
                             username=username,password=password)
    ur.save()
    return render(request,"userregistration.html",{"msg":"User added"})


def userlogin(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    ur=UserregistrationModel.objects.filter(username=username,password=password)
    if not ur:
        return render(request, "userlogin.html", {"message": "Invalid credentials"})
    else:
        return render(request,"healthcareadvisor.html",{"data":ur})


def changeuserpassword(request):
    oldpw=request.POST.get("upassword")
    newpw=request.POST.get("unpassword")
    ur=UserregistrationModel.objects.filter(password=oldpw)
    for x in ur:
        if x.password == oldpw:
            qs=UserregistrationModel.objects.filter(username=x.username).update(password=newpw)
            return render(request, "userlogin.html", {"mssg": "Password updated", "data": qs})
        else:
            return render(request, "changeupwd.html", {"message": "Your old password is incorrect"})
    else:
        return render(request, "changeupwd.html", {"message": "Your old password is incorrect"})

def adminlogin(request):
    username=request.POST.get("uname")
    password=request.POST.get("upass")
    am=AdminModel.objects.filter(username=username,password=password)
    if am:
        return render(request,"welcomeadmin.html",{"data":am})
    else:
        return render(request,"adminlogin.html",{"msg":"Invalid Details"})


def adddisease(request):
    diseaseid=request.POST.get("diseaseid")
    diseasename=request.POST.get("diseasename")
    symptoms=request.POST.get("diseasesymptom")
    dm=DiseaseModel(disease_id=diseaseid,disease_name=diseasename,symptoms=symptoms)
    dm.save()
    return render(request,"adminadddisease.html",{"msg":"Disease added"})


def displayDiseases(request):
    dm=DiseaseModel.objects.all()
    return  render(request,"displaydiseases.html",{"data":dm})

def updatediseases(request):
    id=request.GET.get("id")
    dm=DiseaseModel.objects.filter(disease_id=id)
    return render(request,"updatediseases.html",{"data":dm})


def saveupdateddiseases(request):
    updateddiseaseid=request.POST.get("updatediseaseid")
    updatediseasename=request.POST.get("updatediseasename")
    updatesymptoms=request.POST.get("updatesymptoms")
    dm2=DiseaseModel.objects.filter(disease_id=updateddiseaseid).update(disease_name=updatediseasename,symptoms=updatesymptoms)
    dm = DiseaseModel.objects.all()
    return render(request,"displaydiseases.html",{"data":dm,"msg":"Disease updated successfully"})


def deletedisease(request):
    deld=request.POST.get("deld")
    DiseaseModel.objects.filter(disease_id=deld).delete()
    d=DiseaseModel.objects.all()
    return render(request,"displaydiseases.html",{"data":d})


def addmedicine(request):
    dname=request.POST.get("dname")
    sname=request.POST.get("sname")
    mname=request.POST.get("mname")
    mdes=request.POST.get("mdes")
    mm=MedicineModel(diseasename=dname,symptomname=sname,medicinename=mname,medicinedescription=mdes)
    mm.save()
    return render(request,"addmedicine.html",{"msg":"Medicine added"})


def displaymedicine(request):
    mm=MedicineModel.objects.all()
    return render(request,"modifymedicine.html",{"data":mm})

def updateMedicine(request):
    name = request.GET.get("id")
    qs = MedicineModel.objects.filter(medicinename=name)
    return render(request,"updatemedicineadmin.html",{"data":qs})


def updatemedicineadmin(request):
    mname=request.POST.get("mname")
    mdescr=request.POST.get("mdescr")
    MedicineModel.objects.filter(medicinename=mname).update(medicinedescription=mdescr)
    mm=MedicineModel.objects.filter(medicinename=mname,medicinedescription=mdescr)
    return render(request,"modifymedicine.html",{"msg":"Medicine updated","data":mm})


class DeleteMedicineAdmin(DeleteView):
    template_name = "modifymedicine.html"
    model = MedicineModel
    success_url = '/modifymedicine/'

def displayAll(request):
    mm=MedicineModel.objects.all()
    return render(request,"alldiseasesnmedicinesmenu.html",{"data":mm})



def searchMedicine(request):
    name = request.POST.get("dname")
    mm = MedicineModel.objects.all()
    if mm:
        qs1 = MedicineModel.objects.filter(diseasename=name)
        return render(request,"medicinedetails.html",{"res":qs1})
    else:
        return render(request,"searchmedicineuser.html",{"msg":"Data not available"})