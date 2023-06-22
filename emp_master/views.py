from django.http import HttpResponse, request
from .models import EmpMaster
from django.contrib import messages, auth
from django.shortcuts import redirect, render 
from django.contrib.auth.models import User
from datetime import date, datetime

today = datetime.today()


# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):    
    if request.method == 'POST':
        patient_name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        uhid = request.POST.get('uhid')
        room = request.POST.get('room')
        doctor = request.POST.get('doctor')
        department = request.POST.get('department')
        estimatedTime = request.POST.get('estimatedTime')      
        complaint = request.POST.get('complaint')
        date = today.strftime("%m/%d/%Y, %H:%M")
        status = 'open' 
        # contact = request.POST.get('contact')
    
        user = EmpMaster(DATE=date, PATIENT_NAME=patient_name, GENDER=gender, AGE=age,
                        ROOM_NO=room, UHID_NO=uhid, ADMITTED_UNDER=doctor, DEPARTMENT=department,
                        EST_TIME=estimatedTime, COMPLAINTS=complaint, STATUS=status)
        user.save();
        print('user created')
        return render(request, 'home.html')              # return redirect('/')
    else:
        return render(request, 'register.html')
   
def empMaster(request):   
    lis = EmpMaster.objects.all()
    return render(request, 'empMaster.html', {'lis':lis})

