from django.db.models import Q
from django.shortcuts import render, redirect

from adminapp.models import Faculty,Course
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

from adminapp.models import FacultyCourseMapping
from .models import FacultyStudentMapping

# Create your views here.
def login(request):
    return render(request,'facultylogin.html')

def facultyhome(request):
    fid = request.session["auname"]
    return render(request, 'facultyhome.html',{"fid": fid})

def checkfacultylogin(request):
    fid = request.POST["username"]
    fpwd = request.POST["password"]

    flag = Faculty.objects.filter(Q(facultyid=fid) & Q(password=fpwd))
    if flag:
        request.session["auname"] = fid
        return render(request, "facultyhome.html",{"fid": fid})
    else:
        # return HttpResponse("Login Failed")
        msg = "Login Failed"
        return render(request, "facultylogin.html", {"message": msg})

def signup(request):
    if request.method == 'POST':
        facultyname = request.POST.get('facultyname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'facultylogin.html', {'message': 'Passwords do not match'})

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False  # Deactivate the user until email confirmation
        user.save()

        faculty = Faculty(facultyid = username,fullname=facultyname, email=email, password=password)
        Faculty.save(faculty)
        # Send a registration email
        current_site = get_current_site(request)
        mail_subject = 'SGMS Faculty Account Created'
        message = render_to_string('registration/activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [email])

        # Redirect the user to a page indicating that a confirmation email has been sent
        return render(request, 'facultyhome.html')

    return render(request, 'facultylogin.html')

def facultycourses(request):
    fid = request.session["auname"]
    return render(request, 'facultycourses.html', {"fid": fid})

def facultycourses(request):
    fid = request.session["auname"]
    print(fid)
    courses = Course.objects.all()
    count = Course.objects.count()

    mappingcourses = FacultyCourseMapping.objects.all()
    fmcourses=[]
    for course in mappingcourses:
        if(course.faculty.facultyid==int(fid)):
            fmcourses.append(course)

        print(fmcourses)
        count = len(fmcourses)
    return render(request, "facultycourses.html", {"fid": fid,"fmcourses":fmcourses,"count":count})


def faculty_student_mapping_list(request):
    fid = request.session["auname"]
    faculty = Faculty.objects.get(facultyid=fid)
    faculty_student_mappings = FacultyStudentMapping.objects.filter(faculty_course_mapping__faculty=faculty)
    context = {
        'faculty': faculty,
        'faculty_student_mappings': faculty_student_mappings,
    }

    return render(request, 'faculty_student_mapping_list.html', context)


def addgrade(request):
    if request.method == 'POST':
        mapping_id = request.POST.get('mappingid')
        new_grade = request.POST.get('grade')
        mapping = FacultyStudentMapping.objects.get(mappingid=mapping_id)
        mapping.grade = new_grade
        mapping.save()

        fid = request.session["auname"]
        faculty = Faculty.objects.get(facultyid=fid)
        faculty_student_mappings = FacultyStudentMapping.objects.filter(faculty_course_mapping__faculty=faculty)
        context = {
            'msg' : 'Graded successfully',
            'faculty': faculty,
            'faculty_student_mappings': faculty_student_mappings,
        }

    return render(request, 'faculty_student_mapping_list.html',context)