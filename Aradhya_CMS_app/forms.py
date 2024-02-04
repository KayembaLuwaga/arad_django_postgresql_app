# Aradhya_django/Aradhya_CMS_app/forms.py

from django import forms
from .models import Course, Resource
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']  # Add other fields as needed

# Add other forms as needed

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']

class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'role']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['file', 'description']  # Add other fields as needed
