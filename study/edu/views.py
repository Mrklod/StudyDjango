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
        context = {'student':student}
        return render(request,'list_students.html',context=context)