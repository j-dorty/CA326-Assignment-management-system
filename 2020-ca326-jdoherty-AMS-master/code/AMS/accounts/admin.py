from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

# Register your models here.

class User_Admin(UserAdmin):
    list_display = ('Id','email','username','date_joined','last_login','is_admin','is_staff')
    search_fields = ('Id','email','username')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()          #editing the admin page view to give more details about users and different filter options
    list_filter = ()
    fieldsets = ()

admin.site.register(User, User_Admin) # register the custom user type to the admin page

