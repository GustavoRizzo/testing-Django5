from django.http import HttpResponse

from course.models import Course


def save_course(request):
    name = request.POST.get('name')
    print(f"Saving course with name: {name}")
    obj = Course.objects.create(name=name)
    print(f"Course saved with id: {obj.id}")
    return HttpResponse(f"Course saved successfully, id: {obj.id}")
