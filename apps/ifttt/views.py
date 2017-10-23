# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# All the usuals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

# Misc for IFTTT connection
from dozo.settings import SECRET_KEY, IFTTT_KEY


@login_required(login_url='/')
# IFTTT
def ifttt(request):
    return render(request, 'ifttt/sync.html')


# Configure
def configure(request):
    random = get_random_string(length=8)
    return redirect('')


# Start Session
def start(request):
    
    # Obtain request keys and app key
    client_key = request.GET.get('key', '')
    app_key = SECRET_KEY

    # If keys are matching, confirm member
    if (client_key == app_key):
        device_id = request.body

        # Check device_id against database
        # (CHECK)

        # Check if connection has been recorded in DB
        # If not, record and post success message on dashboard
        # Still leave the device_id on their page

        # Instantiate new session

        return redirect('/')


# End Session
def end(request):
    
    # Obtain request keys and app key
    client_key = request.GET.get('key', '')
    app_key = SECRET_KEY

    # If keys are matching, confirm member
    if (client_key == app_key):
        device_id = request.body

        # Check device_id against database
        return redirect('/')






