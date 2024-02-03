# Aradhya_django/Aradhya_CMS_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Course, Enrollment, Resource, Message, Question, Attendance
from django.contrib import messages
from .forms import CourseForm, UserRegistrationForm, UserAuthenticationForm, ResourceForm
from django.contrib.auth.decorators import login_required, user_passes_test
import  random

def is_admin(user):
    return user.is_authenticated and user.profile.role == 'admin'

@user_passes_test(is_admin)
def add_course(request):
    if request.method == 'POST':
        # Handle form submission to add a new course
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            # Optionally, you can associate the course with the currently logged-in teacher
            course.instructor = request.user
            course.save()
            form.save()
            messages.success(request, 'Course added successfully.')
            return redirect('courses_list')  # Replace 'courses_list' with your courses list URL
    else:
        # Render the form for adding a new course
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

@user_passes_test(is_admin)
def edit_course(request, course_id):
    # Similar logic for editing a course as in add_course view
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully.')
            return redirect('courses_list')  # Replace 'courses_list' with your courses list URL
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form, 'course': course})

@user_passes_test(is_admin)
def delete_course(request, course_id):
    # Logic for deleting a course
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted successfully.')
        return redirect('courses_list')  # Replace 'courses_list' with your courses list URL
    return render(request, 'delete_course.html', {'course': course})

# @login_required(login_url='login')
# def dashboard_view(request):
#     user = request.user
#     if user.role == 'student':
#         # Logic to retrieve enrolled courses for a student
#         courses = user.enrollment_set.all().select_related('course')
#         return render(request, 'student_dashboard.html', {'courses': courses})
#     elif user.role == 'teacher':
#         # Logic to retrieve courses taught by a teacher
#         courses = Course.objects.filter(instructor=user)
#         return render(request, 'teacher_dashboard.html', {'courses': courses})
#     elif user.role == 'admin':
#         # Logic for admin dashboard
#         return render(request, 'admin_dashboard.html')
#     else:
#         # Handle other roles or unauthorized access
#         return render(request, 'home.html')

@login_required(login_url='login')
def student_dashboard(request):
    # Logic to retrieve enrolled courses for a student
    courses = request.user.enrollment_set.all().select_related('course')
    return render(request, 'student_dashboard.html', {'courses': courses})

@login_required(login_url='login')
def teacher_dashboard(request):
    # Logic to retrieve courses taught by a teacher
    courses = Course.objects.filter(instructor=request.user)
    return render(request, 'teacher_dashboard.html', {'courses': courses})

@user_passes_test(is_admin)
def admin_dashboard(request):
    # Logic for the admin dashboard
    return render(request, 'admin_dashboard.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = UserAuthenticationForm(request.POST)
#         if form.is_valid():
#             user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             if user:
#                 login(request, user)
#                 # Redirect based on user role
#                 if user.role == 'student':
#                     return redirect('student_dashboard')  # Change 'dashboard' to the URL for the student dashboard
#                 elif user.role == 'teacher':
#                     return redirect('teacher_dashboard')  # Change 'dashboard' to the URL for the teacher dashboard
#                 elif user.role == 'admin':
#                     return redirect('admin_dashboard')  # Change 'dashboard' to the URL for the admin dashboard
#     else:
#         form = UserAuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            # Default dummy usernames and passwords
            dummy_credentials = [
                {'username': 'Aradhya_Student', 'password': 'pass123', 'role': 'student'},
                {'username': 'Aradhya_Teacher', 'password': 'pass123', 'role': 'teacher'},
                {'username': 'Aradhya_Admin', 'password': 'pass123', 'role': 'admin'},
            ]

            # Find the dummy credentials matching the entered username and password
            entered_username = form.cleaned_data['username']
            entered_password = form.cleaned_data['password']

            matching_credentials = [cred for cred in dummy_credentials if
                                    cred['username'] == entered_username and cred['password'] == entered_password]

            if matching_credentials:
                # Use the first matching credential (you can adjust as needed)
                matching_credential = matching_credentials[0]

                # Authenticate users based on dummy credentials
                user = authenticate(request, username=matching_credential['username'],
                                    password=matching_credential['password'])

                if user:
                    login(request, user)
                    # Assign the role from dummy data
                    user.role = matching_credential['role']
                    user.save()

                    # Redirect based on user role
                    if user.role == 'student':
                        return redirect('student_dashboard')
                    elif user.role == 'teacher':
                        return redirect('teacher_dashboard')
                    elif user.role == 'admin':
                        return redirect('admin_dashboard')
    else:
        form = UserAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required(login_url='login')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Replace 'login' with your login URL

def home_view(request):
    return render(request, 'home.html')  # Replace 'home.html' with the actual template for your home page

@login_required(login_url='login')
def messages_view(request):
    return render(request, 'messages.html')

@login_required(login_url='login')
def courses_list_view(request):
    courses = Course.objects.all()
    enrollments = Enrollment.objects.filter(student=request.user)

    return render(request, 'courses_list.html', {'courses': courses, 'enrollments': enrollments})

def enroll_course(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(pk=course_id)
        student = request.user
        enrollment, created = Enrollment.objects.get_or_create(student=student, course=course)

        if created:
            # Send notification to student
            messages.success(request, f'You have successfully enrolled in {course.name}.')

            return redirect('courses_list')

    return render(request, 'courses_list.html', {'courses': Course.objects.all()})

def grade_course_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollments = Enrollment.objects.filter(course=course)

    if request.method == 'POST':
        for enrollment in enrollments:
            grade = request.POST.get(f'grade_{enrollment.id}')
            if grade is not None:
                enrollment.grade = grade
                enrollment.save()

    return render(request, 'grade_course.html', {'course': course, 'enrollments': enrollments})

def course_detail_view(request, course_id):
    course = Course.objects.get(pk=course_id)
    resources = Resource.objects.filter(course=course)
    return render(request, 'course_detail.html', {'course': course, 'resources': resources})

def upload_resource_view(request, course_id):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.course = Course.objects.get(pk=course_id)
            resource.save()
            return redirect('course_detail', course_id=course_id)
    else:
        form = ResourceForm()
    return render(request, 'upload_resource.html', {'form': form})

def messages_view(request):
    # Add logic to retrieve and display messages
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'messages.html', {'messages': messages})

def ask_question(request, course_id):
    if request.method == 'POST':
        content = request.POST.get('question_content')
        question = Question.objects.create(user=request.user, course_id=course_id, content=content)
        messages.success(request, 'Question submitted successfully.')
        return redirect('courses_list')
    else:
        return render(request, 'ask_question.html', {'course_id': course_id})

@login_required(login_url='login')
def mark_attendance(request, course_id):
    course = Course.objects.get(pk=course_id)

    if request.method == 'POST':
        present_students = request.POST.getlist('present_students')
        for student_id in present_students:
            student = User.objects.get(pk=student_id)
            attendance, created = Attendance.objects.get_or_create(user=student, course=course)
            attendance.present = True
            attendance.save()

        # Redirect to the course details page or another appropriate page
        return redirect('courses_list')

    students = User.objects.filter(role='student')
    attendance_records = Attendance.objects.filter(course=course)

    context = {'course': course, 'students': students, 'attendance_records': attendance_records}
    return render(request, 'mark_attendance.html', context)
