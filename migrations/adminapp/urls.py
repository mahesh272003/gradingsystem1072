"""
URL configuration for sgmsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name="adminlogin"),
    path('home/',views.adminhome,name='adminhome'),


    path("checkadminlogin",views.checkadminlogin,name = "checkadminlogin"),
    path("adminchangepwd",views.adminchangepwd,name = "adminchangepwd"),
    path("adminupdatepwd", views.adminupdatepwd, name="adminupdatepwd"),
    path('adminlogout/', views.logout, name='admin-logout'),

    path("viewcourses", views.viewcourses, name="viewcourses"),
    path("viewfaculty", views.viewfaculty, name="viewfaculty"),
    path("viewstudents", views.viewstudents, name="viewstudents"),

    path("adminstudent", views.adminstudent, name="adminstudents"),
    path("adminfaculty", views.adminfaculty, name="adminfaculty"),
    path("admincourse", views.admincourse, name="admincourses"),

    path("addcourse", views.addcourse, name="addcourse"),
    path("insertcourse", views.insertcourse, name="insertcourse"),

    path("deletecourse/", views.deletecourse, name="deletecourse"),
    path("coursedeletion/<int:cid>/", views.coursedeletion, name="coursedeletion"),

    path("addfaculty", views.addfaculty, name="addfaculty"),
    path("addstudent", views.addstudent, name="addstudent"),

    path("deletefaculty/", views.deletefaculty, name="deletefaculty"),
    path("facultydeletion/<int:fid>/", views.facultydeletion, name="facultydeletion"),

    path("deletestudent/", views.deletestudent, name="deletestudent"),
    path("studentdeletion/<int:sid>/", views.studentdeletion, name="studentdeletion"),

    path("updatecourse",views.updatecourse,name="updatecourse"),
    path("courseupdation/<int:cid>",views.courseupdation,name="courseupdation"),
    path("courseupdated",views.courseupdated,name="courseupdated"),

    path("updatefaculty",views.updatefaculty,name="updatefaculty"),
    path("facultyupdation/<int:fid>",views.facultyupdation,name="facultyupdation"),
    path("facultyupdated",views.facultyupdated,name="facultyupdated"),

    path("updatestudent",views.updatestudent,name="updatestudent"),
    path("studentupdation/<int:sid>",views.studentupdation,name="studentupdation"),
    path("studentupdated",views.studentupdated,name="studentupdated"),

    path("facultycoursemapping", views.facultycoursemapping, name="facultycoursemapping"),
    path("studentcoursemapping", views.studentcoursemapping, name="studentcoursemapping"),

]
