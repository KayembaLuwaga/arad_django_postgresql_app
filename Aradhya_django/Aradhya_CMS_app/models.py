# Aradhya_django/Aradhya_CMS_app/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model


class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    role = models.CharField(max_length=20, choices=ROLES, default='student')

    # Specify unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        related_name='aradhya_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        related_name='aradhya_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return f"{self.username} | {self.get_role_display()}"

class Course(models.Model):
    name = models.CharField(max_length=255)
    # instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taught')
    instructor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='courses_taught')

    # Add other fields as needed

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    # student = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('student', 'course')

    # Add other fields as needed

    def __str__(self):
        return f"{self.student.username} - {self.course.name}"

class Resource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(upload_to='course_materials/')
    description = models.TextField(blank=True)

class Message(models.Model):
    # sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    # receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(get_user_model(), related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(get_user_model(), related_name='received_messages', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Attendance(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=False)
    # Add other fields as needed

    def __str__(self):
        return f"{self.user.username} - {self.course.name} - {self.date}"
