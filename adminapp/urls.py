
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("adminhome" , views.adminhome ,name= "adminhome"),
    path("adminlogout" , views.logout , name = "adminlogout"),
    path("checkadminlogin" , views.checkadminlogin,name = "checkadminlogin"),
    path("viewstudents" , views.viewstudents , name = "viewstudents"),
    path("viewcourses" , views.viewcourses , name = "viewcourses"),
    path("viewfaculty" , views.viewfaculty , name = "viewfaculty"),
    path("admincourses" , views.admincourses,name = "admincourses"),
    path("adminfaculty" , views.adminfaculty,name = "adminfaculty"),
    path("adminstudents" , views.adminstudents,name = "adminstudents"),
    path("addcourses",views.addcourses,name="addcourses"),
    path("updatecourses" , views.updatecourses , name = "updatecourses"),
    path("courseupdation/<int:cid>" , views.courseupdation,name="courseupdation"),
    path("courseupdated" , views.courseupdated , name = "courseupdated"),
    path("insertcourse" , views.insertcourse,name="insertcourse"),
    path("deletecourses" ,views.deletecourses,name="deletecourses"),
    path("coursedeletion/<int:cid>" , views.coursedeletion,name="coursedeletion"),
    path("addfaculty" , views.addfaculty,name="addfaculty"),
    path("deletefaculty" , views.deletefaculty,name="deletefaculty"),
    path("facultydeletion/<int:fid>" , views.facultydeletion,name="facultydeletion"),
    path("updatefaculty",views.updatefaculty,name="updatefaculty"),
    path("facultyupdation/<int:fid>",views.facultyupdation,name="facultyupdation"),
    path("addstudent" , views.addstudent,name="addstudent"),
    path("updatestudent",views.updatestudent,name="updatestudent"),
    path("studentupdation/<int:sid>",views.studentupdation,name="studentupdation"),
    path("deletestudent" , views.deletestudent,name="deletestudent"),
    path("studentdeletion/<int:sid>" , views.studentdeletion,name="studentdeletion"),
    path("facultycoursemapping" , views.facultycoursemapping,name="facultycoursemapping"),
    path("adminchangepwd", views.adminchangepwd,name="adminchangepwd"),
    path("adminupdatepwd" , views.adminupdatepwd,name ="adminupdatepwd"),

]
