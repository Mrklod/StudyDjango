from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import *

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