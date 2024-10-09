from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.create_edit_course, name='create_course'),
    path('course/<int:course_id>/', views.create_edit_course, name='edit_course'),
    path('create_course/', views.create_course, name='create_course'),
]
