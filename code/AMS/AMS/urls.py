from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from accounts.views import *
from assignments.views import *

from accounts.forms import LoginForm

app_name = 'AMS'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploadassignment/', upload_assignment, name='new_assignment'),
    path('about/', views.about, name='about'),
    path('accounts/',include('accounts.urls'), name='accounts'),
    path('assignments/',include('assignments.urls'), name='assignments'),
    path('logout', logout_view, name='logout'),
    path('success', success, name='success'),
    path('uploadgrade/', upload_grade, name='new_grade'),
    path('login', login_view, name='login'),
    path('signup', signup_view, name='signup'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('studentDashboard', studentDashboard_view, name='studentDashboard'),
    path('teacherDashboard', teacherDashboard_view, name='teacherDashboard'),
    path('profile', profile_view, name='profile'),
    path('modules', modules_view, name='modules'),
    path('assignments', assignments_view, name='assignments'),
    path('results', results_view, name='results'),
    path('', views.homepage,name='home'),
   
]

urlpatterns += staticfiles_urlpatterns()