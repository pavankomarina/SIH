
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect
from .forms import *
from django.http import HttpResponse

from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def logout_user(request):
    # form = UserForm(request.POST or None)
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('/login')

def home(request):
    if request.user.is_authenticated():
        return render(request,'index.html',{})
    else:
        messages.success(request,"please login!")
        return render(request,'loginpage.html',{})

def record(request):
    return render(request,'record.html',{})

def loginsample(request):
    if request.method=="POST":
        username=request.POST['username']
        user=User.objects.get(username=username)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request,user)
        messages.success(request,"successful login")
        return redirect('/home')


def login_user(request):
    if request.method == "POST" or request.FILES:
        input_audio=request.FILES['input_audio_file']
        username = request.POST['username']
        user=User.objects.get(username=username)
        password = request.POST['password']
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        userdetails=Userdetails.objects.get(user=User.objects.get(username=username))
        user_audio=userdetails.audio_file
        print(input_audio,user_audio)

        accuracy=33 

        if accuracy>31:

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request,"successful login!")
                    return render(request, 'index.html', {})
            else:
                messages.success(request,"invalid login Details")
                return redirect('/register')
        else:
            messages.success(request,"Voice not matched!")
            return redirect('/register')
    return redirect('/register')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')

def register(request):
    if request.method=="POST" or request.FILES:
        audio_file=request.FILES['audio_file']
        username = request.POST['username']
        password = request.POST['password']
        email=request.POST['email']
        print(username,password,email)
        user=User(username=username)
        user.set_password(password)
        user.email=email
        user.save()
        details=Userdetails()
        details.user=user
        details.audio_file=audio_file
        details.save()
        print("success")
        messages.success(request, "You account has been created!")
        return redirect('/register')
    else:
        return render(request,'registration.html',{})

def comparevoice(request):
    return redirect('/login')





