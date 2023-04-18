from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import  User

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

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))
    class Meta:
        model = User
        fields = ('username','password')

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(initial='Никнейм',widget=forms.TextInput())
    email = forms.CharField(initial= "example@gmail.com",widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    teacher = forms.BooleanField(required=False)
    dekan = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ('username','email','password1','password2','teacher','dekan')
