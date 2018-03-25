

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
# from game.models import *  
from mongoengine import *
#from django.contrib.auth import authenticate
from mongoengine.django.auth import User

from django.contrib.auth import login,logout,authenticate
from mongoengine.django.auth import User
from mongoengine.queryset import DoesNotExist
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt



def logout_user(request):
	# form = UserForm(request.POST or None)
	logout(request)
	context = {
		"sample": 'sample',
	}
	messages.success(request,"Logged out successfully")
	return redirect('/login')

def home(request):
	if request.user.is_authenticated():
		return render(request,'index.html',{})
	else:
		messages.success(request,"please login!")
		return render(request,'loginpage.html',{})

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		#print(username,password)
		user=User.objects.get(username=username)
		user.backend = 'mongoengine.django.auth.MongoEngineBackend'
		if user.password==password:
			login(request,user)
			request.session.set_expiry(60 * 60 * 1)
			#user=authenticate(username=username,password=password)
			#print(user)
			messages.success(request,"successful login!")
			return render(request,'index.html',{})
		else:
			messages.success(request,"invalid login details!")
			return render(request,'loginpage.html',{})
	return render(request,'loginpage.html',{})
	
@csrf_exempt
def register(request):
	if request.method=="POST":
		try:

			username = request.POST['username']
			password = request.POST['password']
			email=request.POST['email']
			user=User()
			user.username=username
			user.password=password
			user.email=email
			user.save()
			messages.success(request, "You account has been created!")
			return redirect('/login')
		except:
			messages.success(request,"Error in creating the account")
			return redirect('/login')
		# return HttpResponseRedirect('/login_user')
	else:
		return render(request,'register.html',{})
