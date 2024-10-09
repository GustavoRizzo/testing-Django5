from django.http import HttpResponse
from django.shortcuts import render

from course.models import Course


def load_list_courses(request):
    courses = Course.objects.all()
    return render(request, './comp_list_all_courses.html', {'courses': courses})


def save_course(request):
    name = request.POST.get('name')
    Course.objects.create(name=name)
    return load_list_courses(request)
