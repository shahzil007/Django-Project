from django.shortcuts import render,redirect
from django.http import HttpResponse
from AssignmentApp.models import Users
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def hello(request):
    return render(request, "hello.html")

def users(request):
    allusers = Users.objects.all()

    context = {'allusers':allusers}

    return render(request, "allusers.html", context)

def adduser(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role']

        Users.objects.create(id=id, name=name, email=email, role=role)
        messages.success(request, 'New user created successfully!')
        return redirect('users') 
    return render(request, 'adduser.html')
