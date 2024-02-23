from django.urls import path
from . import views
urlpatterns = [

    path("studenthome" , views.studenthome,name="studenthome"),
    path("checkstudentlogin",views.checkstudentlogin,name="checkstudentlogin"),
    path("studentchangepwd",views.studentchangepwd,name="studentchangepwd"),
    path("studentupdatepwd",views.studentupdatepwd,name="studentupdatepwd"),
    path("studentcourses",views.studentcourses,name="studentcourses"),
    path("studentcoursecontent",views.studentcoursecontent,name="studentcoursecontent"),
    path("displaystudentcourses",views.displaystudentcourses,name="displaystudentcourses"),

]