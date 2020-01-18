#-*- conding:utf-8 -*-
import time
import sys
from django.contrib               import auth
from django.contrib.auth.hashers  import make_password,check_password
from django.contrib.auth.models   import User
from django.views.decorators.csrf import csrf_exempt
from django.http                  import HttpResponseRedirect, HttpResponse
from django.shortcuts             import render, redirect
from django.contrib               import messages
from django.db.models             import Q
from django.conf                  import settings

# Create your views here.
from .forms         import PatientForm, PForm
from .models        import Patient
from login.models   import Doctor
#sys.path.insert(0, '')
from upload.model.cancer_detection_url import process_image
# from .forms import InfoForm

#import model code
#from .model.cancer_detection_url import process_image

@csrf_exempt
def uploadPage(request, doctorID):
    if request.method == "POST":
        fName       = request.POST.get('fName')
        lName       = request.POST.get('lName')
        gender      = request.POST.get('gender')
        race        = request.POST.get('race')
        ethnicity   = request.POST.get('ethnicity')
        pstatus     = request.POST.get('pstatus')
        remark      = request.POST.get('premark', 'None')
        age         = request.POST.get('age')
        imgURL      = request.POST.get('imgURL')
        doc = Doctor.objects.get(dID = doctorID)
        #print("bafore!!!!!", fName, lName, gender, race, ethnicity, pstatus, age, imgURL)

        if fName != ""  and lName != "":                  #check if user doesn't provide patient's full name
            if gender != "":                              #check if user doesn't provide patient's gender 
                if race != "":                            #check if user doesn't provide patient's race
                    if ethnicity != "":                   #check if user doesn't provide patient's ethnicity
                        if pstatus != "":                 #check if user doesn't provide patient's status
                            if age != None:               #check if user doesn't provide patient's age
                                patientID = "p" + time.strftime("%Y%m%d%H%M%S", time.localtime())

                                #print(sid)
                                #print(patientID, fName, lName, gender, race, ethnicity, pstatus, age)
                                patient = Patient.objects.create(pID=patientID, pFName=fName, pLName=lName, pGender=gender,
                                                                    pRace=race, pEthnicity=ethnicity, pStatus=pstatus, pAge=age, pRemark=remark, pImage=imgURL, dID=doc)  
                                patientName = fName + lName
                                resutlURL = process_image(imgURL, patientName) 
                                patient.resultImg = resutlURL
                                patient.save()                                                                             
                                message = "Database update succeed!!"
                                return render(request, 'upload/upload.html', {"doctorID": doctorID, "backLink" : "../home/" + doctorID, "message" : message})
                            else:
                                message = "Please provide patient's age!"
                                return render(request, 'upload/upload.html', {"doctorID": doctorID, "backLink" : "../home/" + doctorID, "message" : message})                                                   
                        else:
                            message = "Please provide patient's status!"
                            return render(request, 'upload/upload.html', {"doctorID": doctorID, "backLink" : "../home/" + doctorID, "message" : message})
                    else:
                        message = "Please provide patient's ethnicity!"
                        return render(request, 'upload/upload.html', {"doctorID": doctorID, "backLink" : "../home/" + doctorID, "message" : message})
                else:
                    message = "Please provide patient's race!"
                    return render(request, 'upload/upload.html', {"doctorID": doctorID, "backLink" : "../home/" + doctorID, "message" : message})
            else:
                message = "Please provide patient's gender!"
                return render(request, 'upload/upload.html', {"doctorID": doctorID, "backLink" : "../home/" + doctorID, "message" : message})
        else:
            message = "Please provide patient's full name!"
            return render(request, 'upload/upload.html', {"doctorID": doctorID, "backLink" : "../home/" + doctorID, "message" : message})
    else:
        #Patient.objects.all().delete()
        return render(request, 'upload/upload.html', {"doctorID": doctorID, "backLink" : "../home/" + doctorID})
    


