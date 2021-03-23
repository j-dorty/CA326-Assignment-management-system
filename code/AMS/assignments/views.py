from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from . import forms
from django.urls import reverse
import os
from accounts.decorators import role_required

@role_required(allowed_roles=['STD'])
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #handle_uploaded_file(request.POST,request.FILES['file'])
            return HttpResponseRedirect(reverse('assignments:success'))
    else:
        form = UploadFileForm()
    return render(request, 'uploadfile.html', {'form': form})

@role_required(allowed_roles=['STD','TCH'])
def success(request):
    return render(request, 'success.html')

@role_required(allowed_roles=['TCH'])
def upload_assignment(request):
    if request.method == 'POST':
        form = AssignmentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #handle_uploaded_file(request.POST,request.FILES['file'])
            return HttpResponseRedirect(reverse('assignments:success'))
    else:
        form = AssignmentUploadForm()
    return render(request, 'assignmentupload.html', {'form': form})


    
@role_required(allowed_roles=['TCH'])
def upload_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('assignments:success'))
    else:
        form = GradeForm()
    return render(request, 'uploadgrade.html', {'form': form})
