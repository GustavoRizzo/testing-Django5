from django import forms
from django.urls import reverse
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.contrib.admin import site as admin_site
from .models import Course, Student

class CourseForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), required=False, widget=forms.SelectMultiple())

    class Meta:
        model = Course
        fields = ['name', 'students']

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        # Aqui você passa a instância correta do admin_site
        self.fields['students'].widget = RelatedFieldWidgetWrapper(
            self.fields['students'].widget,
            self.fields['students'].queryset.model._meta.get_field('courses').remote_field,  # Corrigido
            reverse('admin:course_student_add'),
            admin_site  # Passando a instância correta do admin_site
        )


class CourseForm2(forms.ModelForm):
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
