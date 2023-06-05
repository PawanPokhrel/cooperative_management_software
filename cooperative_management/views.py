from email import message
import imp
from random import random
from unicodedata import name
from cooperative_management.models import CooperativeCredentials
from cooperative_management.models import EmployeeTable
# from cooperative_management.models import cooperative_credentials
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from random import randint

# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# @login_required


def home(request):
    return render(request, 'cooperativelogin.html')

def cooperativesignup(request):
    return render(request, 'cooperativesignup.html')

def cus_reg(request):
    return render(request, 'cus_reg.html')

# global cid 

def cooperativelogin(request):
    if request.method == "POST":
        email = request.POST['email1']
        password = request.POST['password1']
        print('post vitra xiryo')
        
        try:
            print("try vitra xiryo")
            if CooperativeCredentials.objects.filter(email = email).exists(): 
                print('email check garne vitra xiryo')
                registered_email  = CooperativeCredentials.objects.get(email = email)
                cooperativelogin.cid  = registered_email.id 
                
                print(cooperativelogin.cid)            
                if password == registered_email.password:
                    # messages.success(request, "Success")
                    print("login success")
                    return render (request, 'employeelogin.html')
                else :
                    messages.error(request, "Email or password is wrong. :(")
                    return render(request , 'cooperativelogin.html')

                    
        except Exception as e:
                print(e)
                
    return render(request , 'cooperativelogin.html')

        
    

def employeelogin(request):

       
    if request.method == "POST":
        email = request.POST['email2']
        password = request.POST['password2']
        print('post vitra xiryo')
        
        try:
            print("try vitra xiryo")
            if CooperativeCredentials.objects.filter(email = email).exists(): 
                print('email check garne vitra xiryo')
                registered_email  = CooperativeCredentials.objects.get(email = email)               
                if password == registered_email.password:
                    # messages.success(request, "Success")
                    print("login success")
                    return render (request, 'employeelogin.html')
                else :
                    messages.error(request, 'Email or password is wrong. :(')
                    return render(request , 'cooperativelogin.html')

                    
        except Exception as e:
                print(e)
                
    return render(request , 'cooperativelogin.html')

def employeesignup(request):
    return render(request, 'employeesignup.html')

def register1(request):
    if request.method == "POST":
        # print("Entering...")
        # # if request.POST.get('org_name') and request.POST.get('org_mail') and request.POST.get('org_password'):
        # saverecord = CooperativeCredentials(request.POST)
        # saverecord.name = request.POST.get('org_name')
        # saverecord.email = request.POST.get('org_email')
        # saverecord.password = request.POST.get('org_password')
        # saverecord.save()
        # print("Data uploaded to database")

        name = request.POST['org_name']
        email = request.POST['org_email']
        password = request.POST['org_password']
        confirm_password = request.POST['confirm_password']
        
        
        

        if password != confirm_password :
            print('Password milena')
            messages.error(request, "Password and confirm password are not same.") 
            return render(request, 'cooperativesignup.html')
                           

        else :
            # y = random_with_N_digits(6)
            # send_mail_after_registration(email, y)
            # messages.success(request, "Enter OTP.")
            # return render(request,'cooperativelogin.html')
            # if otp == y :
            #     saverecord = CooperativeCredentials(name=name,email=email,password=password)
            #     saverecord.save()
            #     print(name,email,password)
            #     messages.success(request, "Your account is created successfully.")
            #     return render(request, 'cooperativesignin.html')
            # else :
            #     messages.error(request, "Wrong OTP")
            #     return render(request, 'OTP.html')
                
            # return render(request, 'success.html')
            try:
                # if CooperativeCredentials.objects.filter(name = name).first():
                #     messages.success(request, 'Username is taken.')
                #     return redirect('/cooperativesignup')
                print("trying")
                if CooperativeCredentials.objects.filter(email = email).exists():
                    print("Already Exist")
                    messages.success(request, 'Email is taken.')
                    return render(request, 'cooperativesignup.html')

                else:
                    print("elsing")
                    # if  request.POST.get('org_name') and request.POST.get('org_mail') and request.POST.get('org_password'):
                    saverecord = CooperativeCredentials(name=name,email=email,password=password)
                    saverecord.save()
                    print(name,email,password)
                    messages.success(request, "Your account is created successfully.")
                          #     return render(request, 'cooperativesignin.html')
                        # saverecord = CooperativeCredentials(request.POST)
                        # saverecord.name = request.POST.get('org_name')
                        # saverecord.email = request.POST.get('org_email')
                        # saverecord.password = request.POST.get('org_password')
                        # saverecord.save()
                        # print("Data uploaded to database")
                    auth_token = str(uuid.uuid4())
                    send_mail_after_registration(email , auth_token)
                    return render(request, 'cooperativesignup.html')
            
            except Exception as e:
                print(e)
                
    return render(request , 'cooperativesignup.html')
            
        
        # else:
            # print("Fill the boxes")

 


        # organization_name = request.POST.get('org_name')
        # email = request.POST.get('org_email')
        # password = request.POST.get('org_password')



def register2(request):
    if request.method == "POST":
        # print("Entering...")
        # # if request.POST.get('org_name') and request.POST.get('org_mail') and request.POST.get('org_password'):
        # saverecord = CooperativeCredentials(request.POST)
        # saverecord.name = request.POST.get('org_name')
        # saverecord.email = request.POST.get('org_email')
        # saverecord.password = request.POST.get('org_password')
        # saverecord.save()
        # print("Data uploaded to database")

        name = request.POST['emp_name']
        email = request.POST['emp_email']
        password = request.POST['emp_password']
        confirm_password = request.POST['confirm_password']
        
        
        

        if password != confirm_password :
            print('Password milena')
            messages.error(request, "Password and confirm password are not same.") 
            return render(request, 'employeesignup.html')
                           

        else :
            # y = random_with_N_digits(6)
            # send_mail_after_registration(email, y)
            # messages.success(request, "Enter OTP.")
            # return render(request,'cooperativelogin.html')
            # if otp == y :
            #     saverecord = CooperativeCredentials(name=name,email=email,password=password)
            #     saverecord.save()
            #     print(name,email,password)
            #     messages.success(request, "Your account is created successfully.")
            #     return render(request, 'cooperativesignin.html')
            # else :
            #     messages.error(request, "Wrong OTP")
            #     return render(request, 'OTP.html')
                
            # return render(request, 'success.html')
            try:
                # if CooperativeCredentials.objects.filter(name = name).first():
                #     messages.success(request, 'Username is taken.')
                #     return redirect('/cooperativesignup')
                print("register2 trying")
                if EmployeeTable.objects.filter(name = name).exists():
                    print("Already Exist")
                    messages.success(request, 'Username is taken.')
                    return render(request, 'employeesignup.html')
                if EmployeeTable.objects.filter(email = email).exists():
                    print("Already Exist")
                    messages.success(request, 'Email is taken.')
                    return render(request, 'employeesignup.html')

                else:
                    print("register2 elsing")
                    # if  request.POST.get('org_name') and request.POST.get('org_mail') and request.POST.get('org_password'):
                    saverecord = EmployeeTable(o_id = cooperativelogin.cid, name=name,email=email,password=password)
                    saverecord.save()
                    print(cooperativelogin.cid, name,email,password)
                    messages.success(request, "Your account is created successfully.")
                          #     return render(request, 'cooperativesignin.html')
                        # saverecord = CooperativeCredentials(request.POST)
                        # saverecord.name = request.POST.get('org_name')
                        # saverecord.email = request.POST.get('org_email')
                        # saverecord.password = request.POST.get('org_password')
                        # saverecord.save()
                        # print("Data uploaded to database")
                    auth_token = str(uuid.uuid4())
                    send_mail_after_registration(email , auth_token)
                    return render(request, 'employeesignup.html')
            
            except Exception as e:
                print(e)
                
    return render(request , 'employeesignup.html')

def employeelogin(request):
    if request.method == "POST":
        email = request.POST['email2']
        password = request.POST['password2']
        print('post vitra xiryo')
        
        try:
            print("try vitra xiryo")
            if EmployeeTable.objects.filter(email = email).exists(): 
                print('email check garne vitra xiryo')
                registered_email  = EmployeeTable.objects.get(email = email)
                # cooperativelogin.cid  = registered_email.id 
                # print(cooperativelogin.cid)            
                if password == registered_email.password:
                    # messages.success(request, "Success")
                    print("login success")
                    return render (request, 'window.html')
                else :
                    messages.error(request, "Email or password is wrong. :(")
                    return render(request , 'employeelogin.html')

                    
        except Exception as e:
                print(e)
                
    return render(request , 'cooperativelogin.html')


# def login_attempt(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user_obj = User.objects.filter(username = username).first()
#         if user_obj is None:
#             messages.success(request, 'User not found.')
#             return redirect('/cooperative_management/employeelogin')
        
        
#         profile_obj = Profile.objects.filter(user = user_obj ).first()

#         if not profile_obj.is_verified:
#             messages.success(request, 'Profile is not verified check your mail.')
#             return redirect('/cooperative_management/employeelogin')

#         user = authenticate(username = username , password = password)
#         if user is None:
#             messages.success(request, 'Wrong password.')
#             return redirect('/cooperative_management/employeelogin')
        
#         login(request , user)
#         return redirect('/')

#     return render(request , 'employeelogin.html')

# # def register_attempt(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(password)

#         try:
#             if User.objects.filter(username = username).first():
#                 messages.success(request, 'Username is taken.')
#                 return redirect('/employeesignup')

#             if User.objects.filter(email = email).first():
#                 messages.success(request, 'Email is taken.')
#                 return redirect('/employeesignup')
            
#             user_obj = User(username = username , email = email)
#             user_obj.set_password(password)
#             user_obj.save()
#             auth_token = str(uuid.uuid4())
#             profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
#             profile_obj.save()
#             send_mail_after_registration(email , auth_token)
#             return redirect('/token')

#         except Exception as e:
#             print(e)


#     return render(request , 'employeesignup.html')

# def success(request):
#     return render(request , 'success.html')


# def token_send(request):
#     return render(request , 'token_send.html')



def verify(request , auth_token):
    try:
        saverecord = CooperativeCredentials.objects.filter(auth_token = auth_token).first()
    

        if saverecord:
            if saverecord.is_verified:
                messages.success(request, 'Your account is already verified.')
                return render(request, 'cooperativelogin.html')
            saverecord.is_verified = True
            saverecord.save()
            messages.success(request, 'Your account has been verified.')
            return render(request, 'cooperativelogin.html')
        else:
            return render(request, 'cooperativesignup.html')
    except Exception as e:
        print(e)
        return redirect('/')

# def error_page(request):
#     return  render(request , 'error.html')








def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    

# def send_mail_after_registration(email, x):
#     subject = 'Your accounts need to be verified'
#     message = 'Your OTP is ' + str(x)
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message , email_from ,recipient_list )
    

# def random_with_N_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)
        
    