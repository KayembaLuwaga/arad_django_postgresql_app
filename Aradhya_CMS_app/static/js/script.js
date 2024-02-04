// Aradhya_django/Aradhya_CMS_app/static/js/script.js
$(document).ready(function() {
    // Fetch dummy mirror variables and update the frontend
    function updateMirrorVariables() {
        // Dummy mirror variables
        const dummyVariables = {
            courses: [
                { name: 'Course 1', instructor: 'Instructor 1' },
                { name: 'Course 2', instructor: 'Instructor 2' }
            ],
            grades: [
                { student: 'Student 1', grade: 'Grade 1' },
                { student: 'Student 2', grade: 'Grade 2' }
            ]
        };

        // Update the frontend using dummy mirror variables
        $('#courses-list').html(generateCoursesList(dummyVariables.courses));
        $('#grades-list').html(generateGradesList(dummyVariables.grades));
    }

    // Helper function to generate HTML for the courses list
    function generateCoursesList(courses) {
        let html = '<ul>';
        for (let i = 0; i < courses.length; i++) {
            html += `<li>${courses[i].name} - Instructor: ${courses[i].instructor}</li>`;
        }
        html += '</ul>';
        return html;
    }

    // Helper function to generate HTML for the grades list
    function generateGradesList(grades) {
        let html = '<ul>';
        for (let i = 0; i < grades.length; i++) {
            html += `<li>${grades[i].grade} - Student: ${grades[i].student}</li>`;
        }
        html += '</ul>';
        return html;
    }

    // Call the function to update mirror variables when the page loads
    updateMirrorVariables();
});
