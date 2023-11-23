from django.contrib import admin
from .models import Admin,Course,Faculty,Student,FacultyCourseMapping,StudentCourseMapping

# Register your models here.
admin.site.register(Admin)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(FacultyCourseMapping)
admin.site.register(StudentCourseMapping)
