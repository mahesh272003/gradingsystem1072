from django.db import models
# Create your models here.

class Admin(models.Model):

    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True) #admin
    password=models.CharField(max_length=100,blank=False) #admin

    class Meta:
        db_table="admin_table"

    def __str__(self):
        return self.username

class Course(models.Model):
    id = models.AutoField(primary_key=True)

    department_choices = (("CSE-R", "CSE(Regular)"),("CSE-H", "CSE(Honors)"),("CSIT", "CS&IT"))
    department = models.CharField(max_length=100, blank=False,choices=department_choices)

    academic_choices = (("2022-23", "2022-23"), ("2023-24", "2023-24"))
    academicyear = models.CharField(max_length=20, blank=False,choices=academic_choices)

    program_choices = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
    program = models.CharField(max_length=50, blank=False,choices=program_choices)

    sem_choices = (("ODD","ODD"),("EVEN","EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=sem_choices)

    section = models.CharField(max_length=10, blank=False, help_text="Course section (e.g., A, B, C)")

    year = models.IntegerField(blank=False)
    coursecode = models.CharField(max_length=20, blank=False)
    coursetitle = models.CharField(max_length=50, blank=False)

    ltps = models.CharField(max_length=10 , blank=False)
    credits = models.FloatField(blank=False)

    class Meta:
        db_table="course_table"

    def __str__(self):
        return self.coursecode

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentid=models.BigIntegerField(blank=False,unique=True)
    fullname=models.CharField(max_length=100, blank=False)

    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"),("OTHERS","OTHERS"))
    gender=models.CharField(max_length=20, blank=True,choices=gender_choices)

    department_choices = (("CSE-R", "CSE(Regular)"), ("CSE-H", "CSE(Honors)"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=100, blank=True, choices=department_choices)

    program_choices = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
    program = models.CharField(max_length=50, blank=True,choices=program_choices)

    sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=True, choices=sem_choices)


    year = models.IntegerField(blank=False,default=2)
    password=models.CharField(max_length=100,blank=False,default="klu123")
    email=models.CharField(max_length=100, blank=False,unique=True)
    contact = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table="Student_table"

    def __str__(self):
        return str(self.studentid)

class Faculty(models.Model):

        id = models.AutoField(primary_key=True)
        facultyid = models.BigIntegerField(blank=False, unique=True)
        fullname = models.CharField(max_length=100, blank=True)

        gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))
        gender = models.CharField(max_length=20, blank=True, choices=gender_choices)

        department_choices = (("CSE-R", "CSE(Regular)"), ("CSE-H", "CSE(Honors)"), ("CSIT", "CS&IT"))
        department = models.CharField(max_length=100, blank=True, choices=department_choices)

        qualification_choices = (("Ph.d", "Ph.d"), ("M.Tech", "M.Tech"))
        qualification = models.CharField(max_length=50, blank=True,choices=qualification_choices)

        designation_choices = (("Prof.", "Professor"), ("Assoc. Prof.", "Associate Proffesor"), ("Asst. prof", "Assistant Professor"))
        designation = models.CharField(max_length=50, blank=True,choices=designation_choices)

        sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
        semester = models.CharField(max_length=10, blank=True, choices=sem_choices)

        year = models.IntegerField(blank=True,default=2)
        password = models.CharField(max_length=100, blank=False, default="klu123")
        email = models.CharField(max_length=100, blank=False, unique=True)
        contact = models.CharField(max_length=20, blank=True)

        class Meta:
            db_table="faculty_table"
        def __str__(self):
            return str(self.fullname)


class FacultyCourseMapping(models.Model):
    mappingid = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    component_choices = (("L", "Lecture"), ("T", "Tutorial"), ("P", "Practical"), ("S", "Skill"))
    component = models.CharField(max_length=10, blank=False, choices=component_choices)

    type = models.BooleanField(blank=False, verbose_name="Faculty_name")
    section = models.IntegerField(blank=False)

    class Meta:
        db_table = "facultycoursemapping_table"

    def __str__(self):
        return f"{self.course.coursetitle}-{self.faculty.fullname}"

from django.db import models

class StudentCourseMapping(models.Model):
    mappingid = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "studentcoursemapping_table"

    def __str__(self):
        return f"{self.student.fullname} - {self.course.coursetitle}"
