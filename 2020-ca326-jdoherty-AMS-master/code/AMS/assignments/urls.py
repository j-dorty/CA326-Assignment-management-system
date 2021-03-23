from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'assignments'

urlpatterns = [
    path('uploadassignment/', views.upload_assignment, name='new_assignment'),
    path('uploadfile/', views.upload_file,name='upload'),
    path('success/', views.success, name='success'),
    path('uploadgrade/', views.upload_grade, name='new_grade'),

]