
from django.db import models

from adminapp.models import FacultyCourseMapping,StudentCourseMapping


class FacultyStudentMapping(models.Model):
    mappingid = models.AutoField(primary_key=True)
    faculty_course_mapping = models.ForeignKey(FacultyCourseMapping, on_delete=models.CASCADE)
    student_course_mapping = models.ForeignKey(StudentCourseMapping, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = "facultystudentmapping_table"

    def __str__(self):
        return f"{self.faculty_course_mapping.course.coursetitle} - {self.faculty_course_mapping.faculty.fullname} - {self.student_course_mapping.student.fullname}"
