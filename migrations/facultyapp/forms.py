from django import forms

from facultyapp.models import FacultyStudentMapping


class GradeForm(forms.ModelForm):
    class Meta:
        model = FacultyStudentMapping
        fields = ['grade']