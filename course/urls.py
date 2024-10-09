from django.urls import path
from . import views, htmx_views

urlpatterns = [
    path('list_courses/', views.list_courses, name='list_courses'),
]

htmx_urlpatterns = [
    path('save_course/', htmx_views.save_course, name='save_course'),
    path('load_list_courses/', htmx_views.load_list_courses, name='load_list_courses'),
]

urlpatterns += htmx_urlpatterns
