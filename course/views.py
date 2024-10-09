from django.shortcuts import render, redirect
from .forms import CourseForm, StudentForm
from .models import Course
from django.contrib import messages  # Para mensagens flash


def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'list_courses.html', {'courses': courses})
