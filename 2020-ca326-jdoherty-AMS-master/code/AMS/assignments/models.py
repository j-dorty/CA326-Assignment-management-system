from django.db import models
from accounts.models import User
import uuid  

# Create your models here.

class UploadFile(models.Model): # define a class for the students submissions
    submission_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False) # use the submission id generated automatically and always unique for each submission as the primary key for uploads 
    assignment_id = models.CharField(max_length=15) # link the submission to an assingment instance by including a refernce to the assignment it is meant to be a submission for
    module_id = models.CharField(max_length=15) # link the submission to the module the assingment is for by including a refernce to the module it is meant to be a submission for
    title = models.CharField(max_length=15) # simple title to distinguish between submissions
    submitted_by = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, default='no owner') #attach the id of the student who submitted the submission
    file = models.FileField(upload_to='documents/') # the actual file to be submitted
    uploaded_at = models.DateTimeField(auto_now_add=True) # a time stamo to allow the teacher to check if the submission was submitted within the allotted time period 

class Assignmentupload(models.Model): # define a class for assingment instances created by teachers which give student user types somehting to submit submissions to
    module_id = models.CharField(max_length=15) # the module the assingment is meant to be associated with
    assignment_id = models.CharField(max_length=15) # an id associated with the assignment to allow for look up within the databse
    title = models.CharField(max_length=15) # simple title field
    description = models.CharField(max_length=100) #description of assignmeent what is required by submision etc
    due_date = models.DateTimeField() # due date for submissions to be handed in by

class Grade(models.Model): # define a grade class to allow teachers to give feedbackl on assignments
    module_id = models.CharField(max_length=15) #the module of the assignment the grade refers to
    submission_id = models.CharField(max_length=150) #the unique identifier of submissions allows grades to be assigned to indivual assignemnts
    assignment_id = models.CharField(max_length=15) #id of the assignment the submission was submitted to
    result = models.CharField(max_length=15) #grade field eg 10/10 / 100%
    feedback = models.CharField(max_length=150) #comments or feeback a teacher can give on the assignment