from django.contrib import messages
from django.shortcuts import redirect, render 
from django.http import request 
from django.contrib.auth.models import User
from django.contrib import auth
from emp_master.models import EmpMaster
from pymongo import MongoClient, collection

from datetime import date, datetime
today = datetime.today()


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST['user']
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 == password2:
            if(User.objects.filter(email=email).exists()):
                # messages.info(request,'email taken')
                print('email taken')
                return redirect('/')
            
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password1, username=username)
                user.save();
                print('user created')
                # return redirect('login')
                return redirect('/')
        else:
            print('password not match')
    return render (request, 'signup.html')
    

def login(request):
    if request.method == 'POST':
        username= request.POST['user']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('admin_form')
        else:
            messages.info(request, 'invalid')
            # messages.info(request, 'invalid')
            return redirect('login')

    return render(request, 'login.html')

def empMaster(request):
    lis = EmpMaster.objects.all()
    return render(request, 'empMaster.html', {'lis':lis})


def admin_form(request):
    
# Create your views here.

    if request.method == "POST":
        closure = request.POST.get('closure')
        status = request.POST.get('status')
        resolveDate = today.strftime("%m/%d/%Y")
        remark = request.POST.get('remark')
        comment = request.POST.get('comment')

        print('asdfg')
        try:
            conn = MongoClient()
            print("connected")
        except:
            print("could not connect")

        db = conn.paras
        collection= db.emp_master_empmaster

        result = collection.update_one(
        {"PATIENT_NAME":"aman kumar"},
        {
            "$set":{
                        "COMMENTS": comment,
                        "CLOSURE" : closure,
                        "STATUS" : status,
                        "REMARKS" : remark,
                        "DATE_RESOLVED" : resolveDate,
                        }
        
        }
        )

        print("dATA UPDATED")

        cursor = collection.find()
        for record in cursor:
            print(record)
        

        return redirect('/')
    return render(request, 'admin_form.html')

