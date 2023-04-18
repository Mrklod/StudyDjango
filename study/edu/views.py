from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.http import  HttpResponseRedirect
from .models import *
from .forms import *
class MainView(View):
    def get(self, request):
        return render(request,'main.html')


class ListStudentsView(View):
    def check_scholarship(self,hour_study_week, hour_need):
        average_grade = (hour_study_week / hour_need) * 100
        if average_grade >= 90:
            return True
        else:
            return False

    def get(self, request):
        students = Student.objects.all()
        student_list = []
        for student in students:
            c = self.check_scholarship(student.hour_study_week, student.hour_need)
            student_list.append(c)
        context = {'student_list': student_list,'student':students}
        return render(request, 'list_students.html', context=context)


class ListTeacherView(View):

    def get(self, request):
        teacher = Teacher.objects.all()
        context = {'teacher':teacher}
        return render(request, 'list_teacher.html',context=context)


class NewStudent(View):
    def get(self,request):
        form = StudentForm
        context = {'form':form}
        return render(request,'add_student.html',context=context)

    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('list'))

class NewTeacher(View):
    def get(self,request):
        form = TeacherForm
        context = {'form':form}
        return render(request,'add_teacher.html',context=context)

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('list'))

class NewGroup(View):
    def get(self,request):
        form = GroupForm
        context = {'form':form}
        return render(request,'add_group.html',context=context)

    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('list'))

class RegisterView(View):
    def get(self,request):
        form = UserRegisterForm
        context = {'form': form}
        return render(request, 'register.html', context=context)

    def post(self,request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))



class LoginView(View):
    def get(self,request):
        form = UserLoginForm
        context = {'form': form}
        return render(request, 'login.html', context=context)

    def post(self,request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('main'))
        context = {'form': form}
        return render(request, 'tusk/login.html', context=context)


@method_decorator(login_required,name='dispatch')
class LogoutView(View):
    def get(self,request):
        auth.logout(request)
        return redirect(reverse_lazy('main'))