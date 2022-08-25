import email
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from SSS.models import StudentData

# Create your views here.
def home(request):
    return render(request,'index.html')

def academics(request):
    return render(request,'academics.html')

def infra(request):
    return render(request,'infra.html')

def about(request):
    return render(request,'about.html')


def submitted(request):
    return render(request,'submitted.html')

def userlogin(request):
    if request.method=='POST':
        un=request.POST.get('username')
        pwd=request.POST.get('password') 
        try:
            user=User.objects.get(username=un)
        except:
            messages.info(request,"WRONG CREDENTIALS")
            return redirect('/userlogin')
        user=authenticate(request, username=un, password=pwd)
        if user is not None:
            login(request,user)
            return application(request)  
        else:
            messages.info(request,"WRONG CREDENTIALS")
            return redirect('userlogin')
    else:
        return render(request,'login.html')


def userlogout(request):
    logout(request)
    return render(request,'index.html')

@login_required(login_url='userlogin')
def application(request):

    email=request.user.email
    try:
        s=StudentData.objects.get(email=email)
    except:
        messages.info(request,"WRONG CREDENTIALS")
        return redirect('userlogin')

    if s.sub:
        return render(request,'submitted.html')

    

    if request.method=='POST':
        paymentID=request.POST.get('paymentID')
        fathername=request.POST.get('fathername')
        mothername=request.POST.get('mothername')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        ration=request.POST.get('ration')
        aadhar=request.POST.get('aadhar')
        address=request.POST.get('address')
        birthstate=request.POST.get('birthstate')
        birthdistrict=request.POST.get('district')
        castecert=request.POST.get('castecert')
        minority=request.POST.get('minority')
        ewscert=request.POST.get('ewscert')
        income=request.POST.get('income')
        incomecert=request.POST.get('incomecert')
        bankac=request.POST.get('bankac')
        bankifsc=request.POST.get('bankifsc')
        hsno=request.POST.get('hsno')
        village=request.POST.get('village')
        town=request.POST.get('town')
        pincode=request.POST.get('pincode')
        altmobile=request.POST.get('altmobile')
        yop=request.POST.get('yop')
        medium=request.POST.get('medium')
        school=request.POST.get('school')
        cls6=request.POST.get('cls6')
        cls7=request.POST.get('cls7')
        cls8=request.POST.get('cls8')
        cls9=request.POST.get('cls9')
        cls10=request.POST.get('cls10')
        pref1=request.POST.get('pref1')
        pref2=request.POST.get('pref2')
        pref3=request.POST.get('pref3')
        pref4=request.POST.get('pref4')
        pref5=request.POST.get('pref5')
        pref6=request.POST.get('pref6')
        photo=request.POST.get('photo')
        sign=request.POST.get('sign')
        
        s.paymentID=paymentID
        s.fathername=fathername
        s.mothername=mothername
        s.gender=gender
        s.dob=dob
        s.ration=ration
        s.aadhar=aadhar
        s.address=address
        s.birthsatate=birthstate
        s.birthdistrict=birthdistrict
        s.castecert=castecert
        s.ewscert=ewscert
        s.minority=minority
        s.income=income
        s.incomecert=incomecert
        s.bankac=bankac
        s.bankifsc=bankifsc
        s.hsno=hsno
        s.village=village
        s.town=town
        s.pincode=pincode
        s.altmobile=altmobile
        s.yop=yop
        s.medium=medium
        s.school=school
        s.cls6=cls6
        s.cls7=cls7
        s.cls8=cls8
        s.cls9=cls9
        s.cls10=cls10
        s.pref1=pref1
        s.pref2=pref2
        s.pref3=pref3
        s.pref4=pref4
        s.pref5=pref5
        s.pref6=pref6
        s.photo=photo
        s.sign=sign
        
        s.sub=True
        
        s.save()

        

        return render(request,'submitted.html')

        


    context={
        'mobile':s.mobile,
        'hallticket':s.hallticket,
        'studentname':s.studentname,
        'dob':s.dob,
        'email':email,
        'cat':s.cat,
        'ph':s.ph,
    }
    return render(request,'application_form.html',context)


def counselling(request):
    if request.method=='POST':
        mobile=request.POST.get('mobile')
        hallticket=request.POST.get('hallticket')
        studentname=request.POST.get('studentname')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        cat=request.POST.get('cat')
        ph=request.POST.get('ph')
        try:
            user=User.objects.create_user(username=mobile,password=hallticket,email=email,first_name=studentname)
        except:
            messages.info(request,"SOMETHING WENT WRONG")
            return redirect('userlogin')

        obj=StudentData.objects.create(username=mobile,mobile=mobile,hallticket=hallticket,studentname=studentname,dob=dob,email=email,cat=cat,ph=ph)

        login(request,user)
        return render(request,'application_form.html')
    return render(request,'counselling_form.html')