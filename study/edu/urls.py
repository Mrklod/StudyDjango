from django.urls import path
from .views import *


urlpatterns = [
    path('',MainView.as_view(),name='main'),
    path('list_students',ListStudentsView.as_view(),name='list'),
    path('new_student',NewStudent.as_view(),name='new_student')
]