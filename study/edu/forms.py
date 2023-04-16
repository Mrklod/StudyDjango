from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name","group","study_week","hour_study_week","count_subject","pay_for_study")

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("name","group")

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("name",)