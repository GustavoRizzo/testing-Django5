from django import forms
from django.urls import reverse
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.contrib.admin import site as admin_site
from .models import Course, Student


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'students']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.all()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']
