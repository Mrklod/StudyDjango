from django.urls import path
from .views import *


urlpatterns = [
    path('',MainView.as_view(),name='main'),
    path('list_students/',ListStudentsView.as_view(),name='list'),
    path('list_teacher/',ListTeacherView.as_view(),name='teacher'),
    path('new_student/',NewStudent.as_view(),name='new_student'),
    path('new_teacher/',NewTeacher.as_view(),name='new_teacher'),
    path('new_group/',NewGroup.as_view(),name='new_group'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('personal/',PersonalView.as_view(),name='personal')
]