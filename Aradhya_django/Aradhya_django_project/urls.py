# Aradhya_django/Aradhya_django_project/urls.py
# URL configuration for Aradhya_django_project project.

from django.contrib import admin
from django.urls import path, include
from Aradhya_CMS_app.views import register_view, login_view, logout_view, home_view, \
    add_course, edit_course, delete_course, courses_list_view, \
    messages_view, enroll_course, grade_course_view, ask_question, mark_attendance, \
    student_dashboard, teacher_dashboard, admin_dashboard #, dashboard_view

urlpatterns = [
    path('', home_view, name='home'),
    # path('dashboard/',  dashboard_view, name='dashboard'),
    path('messages/',  messages_view, name='messages'),
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Include other URLs for your project pages
    path('add_course/', add_course, name='add_course'),
    path('courses_list/', courses_list_view, name='courses_list'),
    path('edit_course/<int:course_id>/', edit_course, name='edit_course'),
    path('enroll_course/<int:course_id>/', enroll_course, name='enroll_course'),
    path('delete_course/<int:course_id>/', delete_course, name='delete_course'),
    path('ask_question/<int:course_id>/', ask_question, name='ask_question'),
    path('mark_attendance/<int:course_id>/', mark_attendance, name='mark_attendance'),
    path('grade_course/<int:course_id>/', grade_course_view, name='grade_course'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('teacher_dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),

]
