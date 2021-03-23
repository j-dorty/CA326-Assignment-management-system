from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup_view(request):
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def about(request):
    return render(request, 'about.html')

def homepage(request):
    return render(request, 'homepage.html')