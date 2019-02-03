from django.shortcuts import render
from .models import *
from django.http import *

#Taking the input through html page for the registration of new user and saving it.

def userreg(request):

    if request.method=='POST':
        obj=signupdata()
        fullname=request.POST['T1']
        username=request.POST['T2']
        email=request.POST['T3']
        password=request.POST['T4']
        obj.fullname=fullname
        obj.username=username
        obj.email=email
        obj.password=password
        obj.save()
        return render(request,'Signup.html',{'data':"Success"})
    else:
        return render(request,'Signup.html')
#Taking the input through html page for the registration of new admin and saving it.

def adminreg(request):

    if request.method=='POST':
        obj=admindata()
        name=request.POST['T1']
        address=request.POST['T2']
        contact=request.POST['T3']
        email=request.POST['T4']
        password=request.POST['T5']
        obj.name=name
        obj.address=address
        obj.contact=contact
        obj.email=email
        obj.password=password
        obj.save()
        return render(request,'AdminReg.html',{'data':"Success"})
    else:
        return render(request,'AdminReg.html')

#Redirecting the user to admin home or user home according to the usertype otherwise redirecting back to the login form.

def login(request):
    if request.method=='POST':
        email=request.POST['T1']
        password=request.POST['T2']
        obj=logindata.objects.get(email=email,password=password)
        usertype=obj.usertype
        request.session['usertype']=usertype
        request.session['email']=email
        if usertype=='admin':
            return HttpResponseRedirect('/adminhome/')
        elif usertype=='user':
            return HttpResponseRedirect('/userhome/')
    else:
        return render(request, 'Loginform.html')


#If the usertype is admin, the user is redirected to admin home otherwise error is shown.

def adminhome(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype=='admin':
            return render(request,'AdminHome.html')
        else:
            return render(request,'AuthError.html')
    else:
        return render(request, 'AuthError.html')

#If the usertype is admin, the user is redirected to user home for chatting otherwise error is shown.

def userhome(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype=='user':
            return render(request,'UserHome.html')
        else:
            return render(request,'AuthError.html')
    else:
        return render(request, 'AuthError.html')

#logging out the user, redirecting to the login page

def logout(request):
    try:
        del request.session['email']
        del request.session['usertype']
    except:
        pass
    return HttpResponseRedirect('/login/')


