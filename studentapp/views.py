from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from adminapp.models import StudentCourseMapping
from facultyapp.models import FacultyStudentMapping

# Create your views here.
def login(request):
    return render(request,'studentlogin.html')

def studenthome(request):
    sid = request.session["auname"]
    return render(request, 'studenthome.html',{"sid": sid})

def checkstudentlogin(request):
    sid = request.POST["username"]
    spwd = request.POST["password"]

    flag = Student.objects.filter(Q(studentid=sid) & Q(password=spwd))
    if flag:
        request.session["auname"] = sid
        return render(request, "studenthome.html",{"sid": sid})
    else:
        # return HttpResponse("Login Failed")
        msg = "Login Failed"
        return render(request, "studentlogin.html", {"message": msg})

def signup(request):
    if request.method == 'POST':
        facultyname = request.POST.get('studentname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'studentlogin.html', {'message': 'Passwords do not match'})

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False  # Deactivate the user until email confirmation
        user.save()

        student1 = Student(studentid = username,fullname=facultyname, email=email, password=password)
        Student.save(student1)
        # Send a registration email
        current_site = get_current_site(request)
        mail_subject = 'SGMS Student Account Created'
        message = render_to_string('registration/activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [email])

        # Redirect the user to a page indicating that a confirmation email has been sent
        return render(request, 'studenthome.html')

    return render(request, 'studentlogin.html')

def studentcourses(request):

    sid = request.session["auname"]
    print(sid)
    courses = Course.objects.all()
    count = Course.objects.count()

    mappingcourses = StudentCourseMapping.objects.all()
    smcourses = []
    for course in mappingcourses:
        if (course.student.studentid == int(sid)):
            smcourses.append(course)

        print(smcourses)
        count = len(smcourses)
    return render(request, "studentcourses.html", {"sid": sid, "smcourses": smcourses, "count": count})



def student_grade_mapping_list(request):
    sid = request.session["auname"]
    student = Student.objects.get(studentid=sid)
    student_grade_mapping = FacultyStudentMapping.objects.filter(student_course_mapping__student=student)
    context = {
        'student': student,
        'student_grade_mapping': student_grade_mapping,
    }
    return render(request, 'student_grade_mapping_list.html', context)

def studentchangepwd(request):
    sid = request.session["auname"]
    return render(request,"studentchangepwd.html",{ "sid": sid})

def studentupdatepwd(request):
    sid = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    print(sid,opwd,npwd)
    flag= Student.objects.filter(Q(studentid=sid)&Q(password=opwd))
    if flag:
        print("Old pwd is correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("updated...")
        msg="Password Updated Successfully"
    else:
        print("Old pwd is invalid")
        msg="Old Password Incorrect"
    return render(request,"studentchangepwd.html",{"sid":sid,"msg":msg})

