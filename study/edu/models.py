from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    study_week_need = models.PositiveIntegerField(default=10)
    study_week = models.PositiveIntegerField(default=0)
    hour_need = models.PositiveIntegerField(default=20)
    hour_study_week = models.PositiveIntegerField(default=0)
    subject_need = models.PositiveIntegerField(default=8)
    count_subject = models.PositiveIntegerField(default=0)
    pay_for_study = models.BooleanField(default=True)


    def __str__(self):
        return self.name
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Dekan(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

