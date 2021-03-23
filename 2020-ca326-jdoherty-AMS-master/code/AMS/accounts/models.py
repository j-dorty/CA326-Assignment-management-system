from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, Id, email, username, user_type, password=None):
        if not email:                                                   #create user method called from terminal allow us to set up users with accounts
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')         #custom user manager used to cretae users and super users
                                                                    # needed in order to properly implement a custom user model needed for this project
        user =  self.model(Id=Id,
                email=self.normalize_email(email),
                username=username,
                user_type=user_type
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Id, email, username,user_type, password):        #create superuser method (create user method but with extra permissions) allows us to create an admin type user from the temrinal
        user =  self.create_user(Id=Id,
            email=self.normalize_email(email),
            password=password,
            username=username,
            user_type='TCH'
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):                   #custom user model for this project instead of built in as extra functionality was needed such as multiple user types atrributes membership etc
    Id = models.CharField(primary_key=True, max_length=32, default='blank_id', unique=True)
    email = models.EmailField(max_length=60)
    username = models.CharField(max_length=30)
    #password = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)         #required attributes if a custom user model is implemented
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #first_name = models.CharField     
    
    TEACHER = 'TCH'
    STUDENT = 'STD'                             #2 user types teacher/student
    USER_TYPE_CHOICES = [
        (STUDENT, 'STUDENT'),
        (TEACHER, 'TEACHER')
    ]

    user_type = models.CharField(max_length=3, choices=USER_TYPE_CHOICES, default=STUDENT)

    USERNAME_FIELD = 'Id'           #using a users id and their login field
    REQUIRED_FIELDS = ['email','username','user_type']

    objects = MyUserManager() # set the custom user manager as the controlor for the custom user model

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):     # required functions if a custom user model is implemented
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    def is_teacher(self):
        return self.user_type == "TCH"
    
    def is_student(self):
        return self.user_type == "STD"



class Module(models.Model):         # defining a Module as a group with one teacher type user and many student type users
    module_Id = models.CharField(max_length=5, primary_key=True, unique=True) # module id used as its primary key as this is a unique attribute
    name = models.CharField(max_length=128)
    students = models.ManyToManyField(User, through='Membership',through_fields=('module','student'))   #associating students to modules through memebership class
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher")


    def __str__(self):
        return self.name
"""
    @classmethod
    def create(cls, module_Id, name, teacher):
        module = cls(module_Id=module_Id, name=name,teacher=teacher)
        module.save()
        return module
"""
#    def add_student()
    


class Membership(models.Model): # a class to define the relationship of a student to a module class
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE) # neccesary in order to have  or ethan one student per module
    date_joined = models.DateField()