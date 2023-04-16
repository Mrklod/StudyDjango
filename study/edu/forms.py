from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name","group","study_week","hour_study_week","count_subject","pay_for_study")