from django import forms
from .models import Course, Student

class CourseForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), required=False, widget=forms.SelectMultiple())

    class Meta:
        model = Course
        fields = ['name', 'students']

