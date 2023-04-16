from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
class MainView(View):
    def get(self, request):
        return render(request,'main.html')


class ListStudentsView(View):

    def get(self,request):
        student = Student.objects.all()
        for i in student:
            posesh = (i.hour_study_week / i.hour_need) * 100
        context = {'student':student,'poshesh':posesh}
        return render(request,'list_students.html',context=context)

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