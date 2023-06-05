from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import *
# from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' ,  home  , name="cooperativelogin"),
    path('cooperativesignup' , cooperativesignup , name="cooperativesignup"),
    path ('cooperativelogin', cooperativelogin, name="cooperativelogin"),
    path('employeelogin', employeelogin, name="employeelogin"),
    path('employeesignup', employeesignup, name="employeesignup"),
    path('register1', register1, name="register1"),
    path('register2', register2, name="register2"),
    path('cus_reg', cus_reg, name="cus_reg")

    
    # path('', register_attempt, name="register_attempt")

    # path('employeelogin' , login_attempt , name="login_attempt"),
    # path('token' , token_send , name="token_send"),
    # path('success' , success , name='success'),
    # path('verify/<auth_token>' , verify , name="verify"),
    # path('error' , error_page , name="error")
]
