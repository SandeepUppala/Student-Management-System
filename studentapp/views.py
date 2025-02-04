from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course
from facultyapp.models import CourseContent


# Create your views here.
def studenthome(request):
    sid = request.session["sid"]
    student = Student.objects.get(student_id=sid)
    print(student)
    return render(request ,"studenthome.html",{"sid":sid ,"student":student} )

def checkstudentlogin(request):
    sid = request.POST['sid']
    pwd = request.POST['pwd']

    flag = Student.objects.filter(Q(student_id = sid)&Q(password = pwd))
    print(flag)
    if(flag):
        print("login Success")
        request.session["sid"] = sid #creating session variable
        student = Student.objects.get(student_id=sid)
        print(student)
        return render(request , "studenthome.html" ,{"sid":sid,"student":student})
    else:
        msg = "Login Failed"
        return render(request,"studentlogin.html" , {"message":msg })

def studentchangepwd(request):
    sid = request.session["sid"]
    return render(request,"studentchangepwd.html",{"sid":sid})

def studentupdatepwd(request):
    sid = request.session["sid"]
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(sid,opwd,npwd)
    flag = Student.objects.filter(Q(student_id=sid)&Q(password = opwd))
    if flag:
        print("old password is Correct")
        Student.objects.filter(student_id=sid).update(password=npwd)
        print("Updated....")
        msg = "Password Updated Successfully!"
    else:
        print("Old password is Wrong")
        msg = "Old Password is Incorrect"
    return render(request,"studentchangepwd.html",{"sid":sid,"message":msg})

def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})

def studentcoursecontent(request):
    sid = request.session["sid"]
    content = CourseContent.objects.all()
    return render(request,"studentcoursecontent.html",{"sid":sid , "coursecontent":content})

def displaystudentcourses(request):
    sem=request.POST["sem"]
    ay = request.POST["ay"]
    sid = request.session["sid"]
    courses = Course.objects.filter(Q(semester = sem)&Q(academicyear = ay))
    return render(request,"displaystudentcourses.html",{"courses":courses,"sid":sid})


