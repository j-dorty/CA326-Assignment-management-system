from django import forms
from . import models



class UploadFileForm(forms.ModelForm):                                                     # define a form to be used for assingment submission uploads
    class Meta:
        model = models.UploadFile                                                         #define the model the form will inherit from
        fields = ['module_id','assignment_id','title', 'file','submitted_by']             # define the required inputs for the form

class AssignmentUploadForm(forms.ModelForm):                                             # define a form to be used for assignment creation by teachers for students uploads
    class Meta:
        model = models.Assignmentupload                                                  #define the model the form will inherit from
        fields = ['module_id','assignment_id','title','description','due_date']          # define the required inputs for the form

class GradeForm(forms.ModelForm):                                                        # define a form to be used for submission grades to be uploaded by teachers for students to view
    class Meta:
        model = models.Grade                                                            #define the model the form will inherit from
        fields = ['module_id','assignment_id','submission_id','result','feedback']      # define the required inputs for the form