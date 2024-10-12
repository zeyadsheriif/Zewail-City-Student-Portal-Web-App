from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    student_id = request.form.get('student_id')
    password = request.form.get('password')
    
    if not student_id or not password:
        return "Error: All fields are required.", 400
    
    if len(student_id) != 9 or not student_id.isdigit():
        return "Error: Student ID must be 9 digits.", 400
    
    return f"Student ID: {student_id}, Password: {password}"

if __name__ == '__main__':
    app.run(debug=True)
