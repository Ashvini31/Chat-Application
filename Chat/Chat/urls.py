from django.contrib import admin
from django.urls import path
from app1.views import *


#Mapping between urls and views
#Register all the names of functions of views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userreg/',userreg),
    path('adminreg/',adminreg),
    path('adminhome/',adminhome),
    path('userhome/',userhome),
    path('login/',login),
    path('logout/',logout),
]

