from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm

def create_edit_course(request, course_id=None):
    if course_id:
        course_instance = Course.objects.get(id=course_id)
    else:
        course_instance = None

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course_instance)
        if form.is_valid():
            form.save()
            return redirect('list_courses')  # redirect to the list of courses
    else:
        form = CourseForm(instance=course_instance)

    # return render(request, 'course_form.html', {})
    return render(request, 'course_form.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import CourseForm, StudentForm
from django.contrib import messages  # Para mensagens flash


def create_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        student_form = StudentForm(request.POST)
        if course_form.is_valid() and student_form.is_valid():
            course = course_form.save()
            student = student_form.save()
            course.students.add(student)
            messages.success(request, 'Curso e Aluno criados com sucesso!')  # Mensagem flash
            return redirect('lista_turmas')  # ou outra URL
        else:
            messages.error(request, 'Formulário inválido. Por favor, verifique os erros.')  # Mensagem flash
    else:
        course_form = CourseForm()
        student_form = StudentForm()
    return render(request, 'create_course.html', {'course_form': course_form, 'student_form': student_form})


def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'list_courses.html', {'courses': courses})