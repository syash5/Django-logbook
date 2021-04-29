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
from datetime import tzinfo, timedelta, datetime


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
        # print("x")
        form = LogCreationForm(request.POST)
        # form.fields['user'].initial =  request.user
        # print(form.fields['user'].initial)
        # print("x")
        if form.is_valid():
                start=form.cleaned_data.get("startt")
                end=form.cleaned_data.get("endt")
                # user=form.cleaned_data.get("user")
                # print("x")
                # form.cleaned_data['user'] = request.user
                days = (end-start).days
                seconds = (end-start).seconds

                ZERO = timedelta(0)
                class UTC(tzinfo):
                    def utcoffset(self, dt):
                        return ZERO
                    def tzname(self, dt):
                        return "UTC"
                    def dst(self, dt):
                        return ZERO

                utc = UTC()
                now = datetime.now(utc)
                diffday = (start - now).days
                diffseconds = (start - now).seconds
                # hours = seconds//3600
                # minutes = (seconds//60)%60
                print(days,"days start-end")
                print(diffday,"diffday from today")
                print(diffseconds,"diffday from sec")
                diffseconds
                # print(seconds)
                if(diffday<0):
                    context["error"] = "End task date is less than starting. Please Correct it and Click on Submit !!"
                    return render(request,"logs/form.html",context)
                elif(days==0 and seconds<=60):
                    context["error"] = "The time to complete the project is less than 2 min.. Please Correct it and Click on Submit !!"
                    return render(request,"logs/form.html",context)
                elif(days<0):
                    context["error"] = "End task date is less than starting.. Please Correct it and Click on Submit !!"
                    return render(request,"logs/form.html",context)
                else:
                    user = form.save(commit=False)
                    user.user = request.user
                    user.save()
                    # form.save()
                    # return render(request, "logs/form.html", context)

                return HttpResponseRedirect(reverse('show'))

    else:
        form = LogCreationForm()
    return render(request,'logs/form.html',{'form':form})


@login_required(login_url="/login/")
def show(request):
    # todotask = LogEntry.objects.all()
    # user = request.user

    todotask = LogEntry.objects.filter(user=request.user)

    # print(user.username)
    # print(user.full_name)
    # print(user.email)
    # print(type(todotask.first))
    # print(todotask.first.date())
    # print(todotask.first.startt.date())
    
    for todo in todotask:
        # print(todo.timercount)

        ZERO = timedelta(0)
        class UTC(tzinfo):
            def utcoffset(self, dt):
                return ZERO
            def tzname(self, dt):
                return "UTC"
            def dst(self, dt):
                return ZERO

        utc = UTC()
        now = datetime.now(utc)
        timer = todo.endt - now
        todo.timer = timer
        # lists = []
        # lists.append(timer)
        # context['voted_links'] = timer
        # print(timer)
    # querysetlist = list(todotask)
    # zippedlist = zip(todotask, querysetlist)
    # print(todotask)

    return render(request,"logs/show.html",{'todotask': todotask})


# Dates: 2021-04-13 06:00:00+00:00 2021-04-14 12:00:00+00:00

# from django import template

# register = template.Library()
# @register.filter(name='zip')
# def zip_lists(a, b):
#     return zip(a, b)


