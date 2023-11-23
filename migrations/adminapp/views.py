from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddFacultyForm, AddStudentForm

from .models import Admin, Course, Student, Faculty, FacultyCourseMapping, StudentCourseMapping


# Create your views here.
def login(request):
    return render(request, 'adminlogin.html')


def logout(request):
    return render(request, 'adminlogin.html')


def adminhome(request):
    auname = request.session["auname"]
    return render(request, 'adminhome.html', {"adminuname": auname})


def checkadminlogin(request):
    adminuname = request.POST["username"]
    adminpwd = request.POST["password"]

    flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    if flag:
        print("Login Success")
        request.session["auname"] = adminuname
        return render(request, "adminhome.html", {"adminuname": adminuname})
    else:
        # return HttpResponse("Login Failed")
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"message": msg})

def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{ "adminuname": auname})

def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    print(auname,opwd,npwd)
    flag= Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("Old pwd is correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("updated...")
        msg="Password Updated Successfully"
    else:
        print("Old pwd is invalid")
        msg="Old Password Incorrect"
    return render(request,"adminchangepwd.html",{"adminuname":auname,"msg":msg})
def viewstudents(request):
    students = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request, "viewstudents.html", {"studentdata": students, "count": count, "adminuname": auname})


def viewfaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request, "viewfaculty.html", {"facultydata": faculty, "count": count, "adminuname": auname})


def viewcourses(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request, "viewcourses.html", {"coursesdata": courses, "count": count, "adminuname": auname})


def adminstudent(request):
    auname = request.session["auname"]
    return render(request, "adminstudent.html", {"adminuname": auname})


def adminfaculty(request):
    auname = request.session["auname"]
    return render(request, "adminfaculty.html", {"adminuname": auname})


def admincourse(request):
    auname = request.session["auname"]
    return render(request, "admincourse.html", {"adminuname": auname})


def addcourse(request):
    auname = request.session["auname"]
    return render(request, "addcourse.html", {"adminuname": auname})


def insertcourse(request):
    dept = request.POST["dept"]
    ay = request.POST["ay"]
    program = request.POST["program"]
    sem = request.POST["sem"]
    year = request.POST["year"]
    ccode = request.POST["ccode"]
    ctitle = request.POST["ctitle"]
    ltps = request.POST["ltps"]
    credits = request.POST["credits"]
    course = Course(department=dept, academicyear=ay, program=program, semester=sem, year=year, coursecode=ccode,
                    coursetitle=ctitle, ltps=ltps, credits=credits)

    Course.save(course)

    message = "Course Added Successfully"

    return render(request, "addcourse.html", {'msg': message})


def deletecourse(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    # print(courses)
    return render(request, "deletecourse.html", {"coursesdata": courses, "count": count, "adminuname": auname})
def coursedeletion(request, cid):
    Course.objects.filter(id=cid).delete()
    print(f"Deleted course with ID: {cid}")
    return redirect("deletecourse")


def addfaculty(request):
    form = AddFacultyForm()
    auname = request.session["auname"]
    if request.method == "POST":
        form1 = AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            # return HttpResponse("Faculty added successfully")
            message = "Faculty Added Successfully"
            return render(request,"addfaculty.html",{'msg':message , 'form':form,  "adminuname": auname})
        else:
            message = "Failed to add faculty data"
            return render(request, "addfaculty.html", {'msg': message, 'form': form, "adminuname": auname})
    return render(request,"addfaculty.html",{'form':form, "adminuname": auname})


def deletefaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    # print(faculty)
    return render(request, "deletefaculty.html", {"facultydata": faculty, "count": count, "adminuname": auname})
def facultydeletion(request, fid):
    Faculty.objects.filter(id=fid).delete()
    print(f"Deleted faculty with ID: {fid}")
    return redirect("deletefaculty")


def addstudent(request):
    form = AddStudentForm()
    auname = request.session["auname"]
    if request.method == "POST":
        form1 = AddStudentForm(request.POST)
        if form1.is_valid():
            form1.save()
            # return HttpResponse("Faculty added successfully")
            message = "Student Added Successfully"
            return render(request,"addstudent.html",{'msg':message , 'form':form,  "adminuname": auname})
        else:
            message = "Failed to add student data"
            return render(request, "addstudent.html", {'msg': message, 'form': form, "adminuname": auname})
    return render(request,"addstudent.html",{'form':form, "adminuname": auname})

def deletestudent(request):
    student = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    # print(student)
    return render(request, "deletestudent.html", {"studentdata": student, "count": count, "adminuname": auname})
def studentdeletion(request, sid):
    Student.objects.filter(id=sid).delete()
    print(f"Deleted student with ID: {sid}")
    return redirect("deletestudent")



def updatecourse(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request, "updatecourse.html", {"coursesdata": courses, "count": count, "adminuname": auname})

def courseupdation(request,cid):
    auname=request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid,"adminuname":auname})

def courseupdated(request):
    auname=request.session["auname"]

    cid=request.POST["cid"]
    courseid=int(cid)
    ctitle=request.POST["ctitle"]
    ltps=request.POST["ltps"]
    credits=request.POST["credits"]

    Course.objects.filter(id=courseid).update(coursetitle=ctitle,ltps=ltps,credits=credits)
    msg="Course Updated Successfully"
    return render(request,"courseupdation.html",{"msg":msg,"adminuname":auname,"cid":cid})

def updatefaculty(request):
    facultys = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request, "updatefaculty.html", {"facultydata": facultys, "count": count, "adminuname": auname})

def facultyupdation(request,fid):
    auname=request.session["auname"]
    return render(request,"facultyupdation.html",{"fid":fid,"adminuname":auname})

def facultyupdated(request):
    auname=request.session["auname"]

    fid=request.POST["fid"]
    facultyid=int(fid)
    dept = request.POST["dept"]
    year = request.POST["year"]
    sem = request.POST["sem"]
    desg = request.POST["desg"]
    Faculty.objects.filter(id=facultyid).update(department=dept,year=year,semester=sem,designation=desg)
    msg="Faculty Updated Successfully"
    return render(request,"facultyupdation.html",{"msg":msg,"adminuname":auname,"fid":fid})

def updatestudent(request):
    students = Student.objects.all()
    count = Student.objects.count()
    sid = request.session["auname"]
    return render(request, "updatestudent.html", {"studentdata": students, "count": count, "sid": sid})

def studentupdation(request,sid):
    auname=request.session["auname"]
    return render(request,"studentupdation.html",{"sid":sid,"adminuname":auname})

def studentupdated(request):
    auname = request.session["auname"]

    sid = request.POST["sid"]
    studentid = int(sid)
    name = request.POST["name"]
    year = request.POST["year"]
    sem = request.POST["sem"]
    Student.objects.filter(id=studentid).update(fullname=name, year=year, semester=sem)
    msg = "Student Updated Successfully"
    return render(request, "studentupdation.html", {"msg": msg, "adminuname": auname, "sid": sid})

def facultycoursemapping(request):
    fmcourses = FacultyCourseMapping.objects.all()
    auname = request.session["auname"]
    return render(request, "facultycoursemapping.html", {"adminuname": auname,"fmcourses":fmcourses})

def studentcoursemapping(request):
    smcourses = StudentCourseMapping.objects.all()
    auname = request.session["auname"]
    return render(request,"studentcoursemapping.html",{"adminuname": auname,"smcourses":smcourses})

