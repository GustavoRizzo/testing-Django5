from django.urls import path
from . import views, htmx_views

urlpatterns = [
    path('course/', views.create_edit_course, name='create_course'),
    path('course/<int:course_id>/', views.create_edit_course, name='edit_course'),
    path('create_course/', views.create_course, name='create_course'),

    path('list_courses/', views.list_courses, name='list_courses'),
]

htmx_urlpatterns = [
    path('save_course/', htmx_views.save_course, name='save_course'),
]

urlpatterns += htmx_urlpatterns
