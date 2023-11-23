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
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name="student-login"),
    path('home/', views.studenthome, name='studenthome'),

    path("checkstudentlogin", views.checkstudentlogin, name="checkstudentlogin"),
    path('studentlogin/', views.login, name='student-login'),
    path('signup/', views.signup, name='signup'),

    path("studentcourses", views.studentcourses, name="studentcourses"),
    path('student_grade_mapping_list/', views.student_grade_mapping_list, name='student_grade_mapping_list'),

    path("studentchangepwd",views.studentchangepwd,name = "studentchangepwd"),
    path("studentupdatepwd", views.studentupdatepwd, name="studentupdatepwd"),


]
