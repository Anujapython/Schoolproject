from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def demo(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,'invaild credentials')
            return redirect('/')
    return render(request,'login.html')

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password == password1:
            if User.objects.filter(password=password).exists():
                messages.info(request, 'password incorrect')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

# Create your views here.


def forms(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        address = request.POST['address']
        phno = request.POST['phno']
        department = request.POST['department']
        course = request.POST['course']
        user=auth.authenticate(name=name, dob=dob, age=age, phno=phno, gender=gender, email=email, address=address, department=department, course=course)
    return render(request, 'form.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def new(request):
    return render(request,'new.html')
