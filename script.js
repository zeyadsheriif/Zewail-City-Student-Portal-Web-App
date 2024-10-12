document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const studentId = document.getElementById('student_id').value;
        const password = document.getElementById('password').value;
        
        if (!studentId || !password) {
            alert('Please fill all fields.');
            event.preventDefault();
            return;
        }

        if (studentId.length !== 9 || isNaN(studentId)) {
            alert('Student ID must be 9 digits.');
            event.preventDefault();
        }
    });
});
