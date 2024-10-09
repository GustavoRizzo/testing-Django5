from django.contrib import admin
from .models import Student, Course
from .forms import CourseForm


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = CourseForm  # Define o formulário customizado
    list_display = ['name', 'students_list']
    search_fields = ['name']
    filter_horizontal = ['students']  # Adiciona um filtro horizontal para a relação Many-to-Many
