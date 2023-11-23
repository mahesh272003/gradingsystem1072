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
    path('',views.login,name="faculty-login"),
    path('home/', views.facultyhome, name='facultyhome'),

    path("checkfacultylogin", views.checkfacultylogin, name="checkfacultylogin"),
    path('facultylogin/', views.login, name='faculty-login'),
    path('signup/', views.signup, name='signup'),
    path("facultycourses", views.facultycourses, name="facultycourses"),

    path("myfcourses", views.facultycourses, name="facultycourses"),

    path('addgrade/', views.addgrade, name='addgrade'),
    path('faculty_student_mapping_list/', views.faculty_student_mapping_list, name='faculty_student_mapping_list'),]
