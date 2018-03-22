# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect
from .models import *
# Create your views here.


def index(request):
	return render(request,'index.html',{})
def loginpage(request):
	return render(request,'loginpage.html',{})
