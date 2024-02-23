from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(Honors)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=20, blank=False, choices=department_choices)
    program_choices = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
    program = models.CharField(max_length=20 , blank=False,choices=program_choices,default="B.Tech")
    academicyear_choices = (("2023-24", "2023-24"), ("2022-23", "2022-23"))
    academicyear = models.CharField(max_length=20, blank=False, choices=academicyear_choices)
    semester_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False, choices=semester_choices)
    year = models.IntegerField(blank=False)
    Coursecode = models.CharField(max_length=20, blank=False)
    CourseTitle = models.CharField(max_length=20, blank=False)
    ltps = models.CharField(max_length=10,blank=False)
    credits = models.FloatField(blank=False)

    class Meta:
        db_table = "Course_table"


    def __str__(self):
        return self.Coursecode


class Student(models.Model):
    id = models.AutoField(primary_key = True)
    student_id = models.BigIntegerField(blank = False , unique = True)
    FullName =  models.CharField(max_length=100,blank = False)
    gender = models.CharField(max_length=20,blank =False)
    department = models.CharField(max_length=20,blank =False)
    Program = models.CharField(max_length=20 , blank = False)
    semester = models.CharField(max_length=20,blank =False)
    year = models.IntegerField(blank = False)
    password = models.CharField(max_length=100 ,blank = False, default = "klu123")
    Email = models.CharField(max_length=100 , blank = False , unique = True)
    contact = models.CharField(max_length=20,unique = True)

    class Meta:
        db_table = "Student_Table"

    def __str__(self):
        return str(self.student_id)

class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    faculty_id = models.BigIntegerField(blank=False, unique=True)
    FullName = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=20, blank=False)
    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(Honors)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=20, blank=False,choices=department_choices)
    Qualification = models.CharField(max_length=20, blank=False)
    designation = models.CharField(max_length=20,blank = False)
    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100, blank=False, default="klu123")
    Email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "Faculty_table"

    def __str__(self):
        return str(self.faculty_id)

class FacultyCourseMapping(models.Model):
    mappingid = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    component_choices = (("L","Lecture"),("T","Tutorial") , ("P","Practical") ,("S","Skill") )
    component = models.CharField(max_length=10,blank=False , choices=component_choices)

    type = models.BooleanField(blank=False , verbose_name="Faculty Type")
    section = models.IntegerField(blank=False)

    class Meta:
        db_table = "facultycoursemapping_table"

    def __str__(self):
        return f"{self.course.CourseTitle}-{self.faculty.FullName}"