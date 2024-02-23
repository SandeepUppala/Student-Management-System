from django import forms
from .models import Faculty, Student


#AddFacultyForm will be created based on Faculty model
class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty  #model name
        fields = "__all__" # all fields in the model , autofield will be hided
        exclude = {"password"} #exclude form box
        labels = {"faculty_id" : "Enter Faculty ID" , "gender" : "Select Gender" , "FullName" : "Enter FullName" , } # changing label names in form

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = {"password"}
        labels = {"student_id" : "Enter Student ID" ,"FullName" : "Enter FullName" ,"gender" : "Gender" ,"department":"Department"}

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = {"student_id"}
class FacultyForm(forms.ModelForm):
    class Meta:
        model= Faculty
        fields = "__all__"
        exclude ={"faculty_id"}