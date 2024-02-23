from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Faculty , FacultyCourseMapping , Course

from facultyapp.models import CourseContent


# Create your views here.
def facultyhome(request):
    fid = request.session["fid"]
    return render(request,"facultyhome.html",{"fid":fid})


def checkfacultylogin(request):
    fid = request.POST['fid']
    pwd = request.POST['pwd']

    flag = Faculty.objects.filter(Q(faculty_id = fid)&Q(password = pwd))
    print(flag)
    if(flag):
        print("login Success")
        request.session["fid"] = fid #creating session variable
        return render(request , "facultyhome.html" ,{"fid":fid})
    else:
        msg = "Login Failed"
        return render(request,"facultylogin.html" , {"message":msg })
        #return HttpResponse("Login fail")

def facultycourses(request):
    fid = request.session.get("fid")

    mappingcourses = FacultyCourseMapping.objects.all()

    fcourses = []
    for course in mappingcourses:
        if course.faculty.faculty_id == int(fid):
            fcourses.append(course)
    print(fcourses)

    dir(fcourses)
    count = len(fcourses)
    return render(request , "facultycourses.html",{"fid":fid , "fcourses":fcourses ,"count":count})

def facultychangepwd(request):
    fid = request.session["auname"]
    return render(request,"facultychangepwd.html",{"fid":fid})

def facultyupdatepwd(request):
    fid = request.session["fid"]
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(fid,opwd,npwd)
    flag = Faculty.objects.filter(Q(faculty_id=fid)&Q(password = opwd))
    if flag:
        print("old password is Correct")
        Faculty.objects.filter(faculty_id=fid).update(password=npwd)
        print("Updated....")
        msg = "Password Updated Successfully!"
    else:
        print("Old password is Wrong")
        msg = "Old Password is Incorrect"
    return render(request,"facultychangepwd.html",{"fid":fid,"message":msg})

