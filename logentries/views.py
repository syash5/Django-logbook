from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from user.forms import UserRegistrationForm
from user.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import json
from django.conf import settings
# import requests
from django.contrib import messages
from logentries.models import *
from logentries.forms import *
import datetime

@login_required(login_url="/login/")
def projectcreate(request):
    if request.method == "POST":
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('show'))
    else:
        form = ProjectCreateForm()
    return render(request,'logs/form.html',{'form':form})

@login_required(login_url="/login/")
def add_log(request):
    context = {}
    if request.method == "POST":
        form = LogCreationForm(request.POST)

        if form.is_valid():
                start=form.cleaned_data.get("startt")
                end=form.cleaned_data.get("endt")

                days = (end-start).days
                seconds = (end-start).seconds
                # hours = seconds//3600
                # minutes = (seconds//60)%60

                if (days<=0 or seconds<60):
                    context["error"] = "End task date is less than starting. Please Correct it and Click on Submit !!"
                    return render(request,"logs/form.html",context)
                    # return render(request, "logs/form.html", context)
                else:
                    form.save()
                    return HttpResponseRedirect(reverse('show'))

    else:
        form = LogCreationForm()
    return render(request,'logs/form.html',{'form':form})


@login_required(login_url="/login/")
def show(request):
    todotask = LogEntry.objects.filter(user=user)

    print(type(todotask.first))
    # print(todotask.first.date())
    # print(todotask.first.startt.date())
    # for todo in todotask:
    #     print(todo.timercount)
        # remaindertime = 

    return render(request,"logs/show.html",{'todotask':todotask})

# Dates: 2021-04-13 06:00:00+00:00 2021-04-14 12:00:00+00:00