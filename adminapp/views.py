from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Admin,Course,Student,Faculty,FacultyCourseMapping
from .forms import AddFacultyForm, AddStudentForm, StudentForm, FacultyForm


# Create your views here.
def adminhome(request):
    auname = request.session["auname"]
    return render(request ,"adminhome.html",{"adminuname":auname} )
def index(request):
    auname = request.session["auname"]
    return render(request,"index.html",{"adminuname":auname})

def logout(request):
    return render(request ,"login.html" )
def checkadminlogin(request):
    adminuname = request.POST['username']
    adminpwd = request.POST['pwd']

    flag = Admin.objects.filter(Q(username = adminuname)&Q(password = adminpwd))
    print(flag)
    if(flag):
        print("login Success")
        request.session["auname"] = adminuname #creating session variable
        return render(request , "adminhome.html" ,{"adminuname":adminuname})
    else:
        msg = "Login Failed"
        return render(request,"login.html" , {"message":msg })
        #return HttpResponse("Login fail")


def viewstudents(request):
    students = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request,"viewstudents.html",{"studentsdata":students , "count":count,"adminuname":auname})
def viewcourses(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request,"viewcourses.html",{"coursesdata":courses, "count":count,"adminuname":auname})
def viewfaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request,"viewfaculty.html",{"facultydata":faculty , "count":count,"adminuname":auname})
def adminstudents(request):
    auname = request.session["auname"]
    return render(request,"adminstudents.html",{"adminuname":auname})
def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,"adminfaculty.html",{"adminuname":auname})
def admincourses(request):
    auname = request.session["auname"]
    return render(request,"admincourses.html",{"adminuname":auname})
def addcourses(request):
    auname = request.session["auname"]
    return render(request,"addcourses.html",{"adminuname":auname})
def updatecourses(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"updatecourses.html" ,{"adminuname":auname , "courses":courses,"count":count})

def courseupdation(request,cid):
    auname = request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid ,"adminuname":auname})
def courseupdated(request):
    auname = request.session["auname"]
    cid = request.POST["cid"]
    courseid = int(cid)
    ctitle = request.POST["ctitle"]
    ltps = request.POST["ltps"]
    credits = request.POST["credits"]
    Course.objects.filter(id=courseid).update(CourseTitle=ctitle,ltps=ltps,credits=credits)
    msg= "Course Updated successfully"
    return render(request,"courseupdation.html",{"msg":msg , "adminuname":auname ,"cid":cid})


def insertcourse(request):
    auname = request.session["auname"]
    if request.method == "POST":
        dept = request.POST["dept"]
        Program = request.POST["program"]
        ay = request.POST["ay"]
        sem = request.POST["sem"]
        year = request.POST["year"]
        ccode = request.POST["ccode"]
        ctitle = request.POST["ctitle"]
        ltps = request.POST["ltps"]
        credits= request.POST["credits"]

        course=Course(department=dept,program=Program,academicyear=ay,semester=sem,year=year,Coursecode=ccode,CourseTitle=ctitle,ltps=ltps , credits = credits)
        Course.save(course)
        message = "Course Added Successfully"
        return render(request,"addcourses.html" ,{"msg" : message,"adminuname":auname})


"""
if request.method = "post":
  name = request .post["uname"]
if request.method = "get":
  name = request.GET["uname"]  
"""
def deletecourses(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request, "deletecourses.html", {"coursesdata": courses, "count": count,"adminuname":auname})
def coursedeletion(request,cid):
    Course.objects.filter(id=cid).delete()

   # return HttpResponse("Course Deleted Successfully")
    return redirect("deletecourses")

def addfaculty(request):
    auname = request.session["auname"]
    form = AddFacultyForm()  #Non Paramerized constructor
    if request.method == "POST":
        form1 = AddFacultyForm(request.POST) #request.POST means form add
        if form1.is_valid():
            form1.save()  #this wll save data in database table
            #return HttpResponse("Faculty Added Succesfully")
            message = "Faculty Added Successfully!"
            return render(request,"addfaculty.html",{"msg":message , "form":form})
        else:
            message = "Failed To Add Faculty"
            return render(request, "addfaculty.html", {"msg": message, "form": form})

    return render(request , "addfaculty.html" , {"form":form ,"adminuname":auname})

def deletefaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request, "deletefaculty.html", {"facultydata": faculty, "count": count,"adminuname":auname})
def facultydeletion(request,fid):
    Faculty.objects.filter(id=fid).delete()

   # return HttpResponse("Course Deleted Successfully")
    return redirect("deletefaculty")


def updatefaculty(request):
    auname = request.session["auname"]
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, "updatefaculty.html", {"facultydata": faculty, "count": count,"adminuname":auname})

def facultyupdation(request,fid):
   auname = request.session["auname"]
   faculty = get_object_or_404(Faculty,pk=fid)
   if request.method == "POST":
       form = FacultyForm(request.POST,instance=faculty)
       if form.is_valid():
           form.save()
           message = "Faculty Updated Successfully!"
           return render(request, "facultyupdated.html", {"msg": message, "form": form, "adminuname": auname})
       else:
           message = "Failed to Update Faculty"
           return render(request, "facultyupdated.html", {"msg": message, "form": form, "adminuname": auname})
   else:
       form = FacultyForm(instance=faculty)
   return render(request,"facultyupdated.html",{"form":form ,"adminuname":auname})


def addstudent(request):
    auname = request.session["auname"]
    form = AddStudentForm()  #Non Paramerized constructor
    if request.method == "POST":
        form1 = AddStudentForm(request.POST) #request.POST means form add
        if form1.is_valid():
            form1.save()  #this wll save data in database table
            #return HttpResponse("Faculty Added Succesfully")
            message = "Student Added Successfully!"
            return render(request,"addstudent.html",{"msg":message , "form":form ,"adminuname":auname})
        else:
            message = "Failed to Add Student"
            return render(request, "addstudent.html", {"msg": message, "form": form, "adminuname": auname})
    return render(request , "addstudent.html" , {"form":form ,"adminuname":auname})

def updatestudent(request):
    auname = request.session["auname"]
    student = Student.objects.all()
    count = Student.objects.count()
    return render(request, "updatestudent.html", {"studentsdata": student, "count": count,"adminuname":auname})

def studentupdation(request,sid):
   auname = request.session["auname"]
   student = get_object_or_404(Student,pk=sid)
   if request.method == "POST":
       form = StudentForm(request.POST,instance=student)
       if form.is_valid():
           form.save()
           message = "Student Updated Successfully!"
           return render(request, "studentupdated.html", {"msg": message, "form": form, "adminuname": auname})
       else:
           message = "Failed to Update Student"
           return render(request, "studentupdated.html", {"msg": message, "form": form, "adminuname": auname})
   else:
       form = StudentForm(instance=student)
   return render(request,"studentupdated.html",{"form":form ,"adminuname":auname})

def deletestudent(request):
    auname = request.session["auname"]
    student = Student.objects.all()
    count = Student.objects.count()
    return render(request, "deletestudent.html", {"studentsdata": student, "count": count,"adminuname":auname})
def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()

   # return HttpResponse("Course Deleted Successfully")
    return redirect("deletestudent")

def facultycoursemapping(request):
    fmcourses = FacultyCourseMapping.objects.all()
    print(fmcourses)
    auname = request.session["auname"]
    return render(request,"facultycoursemapping.html",{"adminuname":auname ,"fmcourses":fmcourses})

def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{"adminuname":auname})

def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(auname,opwd,npwd)
    flag = Admin.objects.filter(Q(username=auname)&Q(password = opwd))
    if flag:
        print("old password is Correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("Updated....")
        msg = "Password Updated Successfully!"
    else:
        print("Old password is Wrong")
        msg = "Old Password is Incorrect"
    return render(request,"adminchangepwd.html",{"adminuname":auname,"message":msg})