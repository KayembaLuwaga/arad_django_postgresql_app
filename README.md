# Aradhya Student Course Management System (SCMS)

Aradhya SCMS is a web-based platform built with Django and PostgreSQL, designed to manage student courses, assignments, and communication between students and instructors.
Table of Contents

    Installation
        PostgreSQL
            Windows
            Linux/Ubuntu
        Project Setup
    Usage
    Project Structure
    Features
    Contributing
    License

## Installation
## PostgreSQL
### Windows

    Download PostgreSQL:
        Visit the official PostgreSQL download page and download the installer.

    Install PostgreSQL:
        Run the installer and follow the on-screen instructions.
        Note the PostgreSQL superuser credentials (username and password) during the installation.

    Download pgAdmin 4:
        Visit the pgAdmin 4 download page and download the installer.

    Install pgAdmin 4:
        Run the installer and follow the on-screen instructions.
        Configure pgAdmin 4 to connect to the PostgreSQL server using the superuser credentials.

### Linux/Ubuntu
1. Install PostgreSQL:
'
sudo apt update
sudo apt install postgresql postgresql-contrib
'
2. Set up PostgreSQL:

    PostgreSQL is automatically started after installation.
    Create a superuser for PostgreSQL:
    '
    sudo -u postgres createuser --interactive
    '
3. Install pgAdmin 4:

    Use the following commands to install pgAdmin 4:
    '
    sudo apt install pgadmin4 pgadmin4-apache2
    '
4. Access pgAdmin 4:

    Open a web browser and go to http://localhost/pgadmin4 after installation.
    Set up a new server connection in pgAdmin 4 using the PostgreSQL superuser credentials.

## Project Setup

1. Clone the Repository:
'
git clone https://github.com/yourusername/Aradhya_django.git
cd Aradhya_django
'
2. Create a Virtual Environment:
'
python -m venv venv
'
3. Activate the Virtual Environment:

    Windows:
    '.\venv\Scripts\activate'

    Linux/Ubuntu:
    'source venv/bin/activate'
4. Install Dependencies:
'pip install -r requirements.txt'
5. Apply Migrations:
'python manage.py listmigrations
python manage.py showmigrations
python manage.py makemigrations
python manage.py migrate'
6. Run the Development Server:
'python manage.py runserver'
7. Access the Application:
Open a web browser and go to http://localhost:8000.

## Usage

1.    Admin Dashboard:
        Access the admin dashboard at http://localhost:8000/admin/.
        Use the superuser credentials mentioned in Aradhya_django/Aradhya_django_project/settings.py.

2.    User Authentication:
        Register and log in with different user roles (students, teachers, admins) to access their respective dashboards.

3.    Course Management:
        Administrators can add, edit, and delete courses.
        Assign instructors/teachers to courses.
        Display a list of available courses.

4.    Enrollment System:
        Students can enroll in courses.
        View a list of enrolled courses.

5.    Grading System:
        Instructors can populate and grade student assignments and exams.
        Display grades to students.

6.    Resource Management:
        Instructors can upload and manage course materials.
        Students can download course materials.

7.    Communication:
        Implement a messaging system for communication between students and instructors.

8.    Attendance Tracking:
        Instructors can mark and track student attendance.
        Display attendance records to students.

9.    Dashboard and Reporting:
        Create personalized dashboards for each user role.
        Generate reports for administrators on course popularity, enrollment statistics, etc.

## Project Structure

####    Aradhya_django_project:
        settings.py: Django project settings, including database configuration.
        urls.py: URL configuration for the project.

####    Aradhya_CMS_app:
        admin.py: Django admin configurations.
        forms.py: Custom forms for user registration and authentication.
        models.py: Database models for User, Course, Enrollment, Assignment, etc.
        views.py: Views for handling different functionalities.

####    Templates:
        HTML templates for different pages, including the base template.

## Features

    User authentication with different roles (admin, staff/teacher, student).
    Course management, enrollment, grading, resource management, and communication features.
    Dashboard and reporting functionalities for administrators, teachers, and students.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License
This project is licensed under the MIT License.
