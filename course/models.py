from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(Student, related_name='courses')

    @property
    def students_list(self):
        return ', '.join([student.name for student in self.students.all()])

    def __str__(self):
        return self.name
