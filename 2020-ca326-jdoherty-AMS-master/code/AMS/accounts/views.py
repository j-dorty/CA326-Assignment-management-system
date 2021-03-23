from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Membership, Module
from assignments.models import Assignmentupload, UploadFile, Grade
from accounts.decorators import role_required


def signup_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #log the user in
            return redirect('accounts:login')

    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            if user.user_type == 'TCH':
                return redirect('teacherDashboard')
            else:
                return redirect('studentDashboard')

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')

@role_required(allowed_roles=['STD'])
def studentDashboard_view(request):
    return render(request, 'accounts/studentDashboard.html')

@role_required(allowed_roles=['TCH'])
def teacherDashboard_view(request):
    return render(request, 'accounts/teacherDashboard.html')


def profile_view(request):
    return render(request, 'accounts/profile.html')

def modules_view(request):

    user = request.user

    teacher_modules = Module.objects.filter(teacher_id=user.Id)
    taught_modules = []
    for e in teacher_modules:
        if e:
            taught_modules.append(e)


    membership = Membership.objects.filter(student_id=user.Id)
    modules = []
    for e in membership:
        if e:
            modules.append(e.module)
    
    context = {

        'taught_modules': taught_modules,
        'modules': modules,
        'student_id' : user.Id,
    }



    return render(request, 'accounts/modules.html',context)

def assignments_view(request):

    context = {}
    user = request.user


    teacher_modules = Module.objects.filter(teacher_id=user.Id)
    taught_modules = []
    for e in teacher_modules:
        taught_modules.append(e.module_Id)
        print(e.module_Id)
    
    created_assignemnts_to_submissions = {}
    for entry in taught_modules:
        assignments = Assignmentupload.objects.filter(module_id=entry)
        for e in assignments:
            created_assignemnts_to_submissions[e] = UploadFile.objects.filter(assignment_id=e.assignment_id)
            
    print(created_assignemnts_to_submissions)
    
    membership = Membership.objects.filter(student_id=user.Id)
    modules = []
    for e in membership:
        modules.append(e.module.module_Id)
    
    mods_ass = []

    for entry in modules:
        assignments = Assignmentupload.objects.filter(module_id=entry)
        if assignments:
            for assignment in assignments:
                mods_ass.append(assignment)
        
    context['created_assignments'] = created_assignemnts_to_submissions
    context['assignments'] = mods_ass
    context['modules'] = modules
    context['student_id'] = user.Id


    return render(request, 'accounts/assignments.html',context)

def results_view(request):

    context = {}

    user = request.user
    uploads = UploadFile.objects.filter(submitted_by=user.Id)
    submission_ids = []
    if uploads:
        for entry in uploads:
            #print(entry.submission_id)
            submission_ids.append("".join(str(entry.submission_id).split('-')))

    results=[]
    for entry in submission_ids:
        grade = Grade.objects.filter(submission_id=entry)
        if grade:
            for e in grade:
                results.append(e)

    context['results'] = results
    context['student_id'] = user.Id


    return render(request, 'accounts/results.html',context)