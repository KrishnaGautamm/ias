class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.activities = []

    # Admission Management
    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student['name']} added successfully.")

    def view_students(self):
        for student in self.students:
            print(student)

    def update_student(self, student_id, updated_info):
        for student in self.students:
            if student['id'] == student_id:
                student.update(updated_info)
                print(f"Student {student_id} updated successfully.")
                return
        print(f"Student {student_id} not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student['id'] == student_id:
                self.students.remove(student)
                print(f"Student {student_id} deleted successfully.")
                return
        print(f"Student {student_id} not found.")

    # Extracurricular Activities
    def add_activity(self, activity):
        self.activities.append(activity)
        print(f"Activity {activity['name']} added successfully.")

    def view_activities(self):
        for activity in self.activities:
            print(activity)

    def assign_student_to_activity(self, student_id, activity_name):
        student_found = False
        activity_found = False

        for student in self.students:
            if student['id'] == student_id:
                student_found = True
                for activity in self.activities:
                    if activity['name'] == activity_name:
                        activity_found = True
                        if 'students' not in activity:
                            activity['students'] = []
                        activity['students'].append(student)
                        print(f"Student {student_id} assigned to activity {activity_name}.")
                        return
        
        if not student_found:
            print(f"Student {student_id} not found.")
        if not activity_found:
            print(f"Activity {activity_name} not found.")

    # Qualified Teaching Staff
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Teacher {teacher['name']} added successfully.")

    def view_teachers(self):
        for teacher in self.teachers:
            print(teacher)

    def update_teacher(self, teacher_id, updated_info):
        for teacher in self.teachers:
            if teacher['id'] == teacher_id:
                teacher.update(updated_info)
                print(f"Teacher {teacher_id} updated successfully.")
                return
        print(f"Teacher {teacher_id} not found.")

    def delete_teacher(self, teacher_id):
        for teacher in self.teachers:
            if teacher['id'] == teacher_id:
                self.teachers.remove(teacher)
                print(f"Teacher {teacher_id} deleted successfully.")
                return
        print(f"Teacher {teacher_id} not found.")


# Example usage
school = SchoolManagementSystem()

# Adding students
school.add_student({'id': 1, 'name': 'John Doe', 'class': '5th Grade'})
school.add_student({'id': 2, 'name': 'Jane Smith', 'class': '6th Grade'})

# Viewing students
school.view_students()

# Updating student details
school.update_student(1, {'class': '6th Grade'})

# Deleting a student
school.delete_student(2)

# Adding extracurricular activities
school.add_activity({'name': 'Basketball', 'coach': 'Mr. Brown'})
school.add_activity({'name': 'Music', 'coach': 'Ms. Green'})

# Viewing activities
school.view_activities()

# Assigning student to activity
school.assign_student_to_activity(1, 'Basketball')

# Adding teachers
school.add_teacher({'id': 1, 'name': 'Mr. Brown', 'subject': 'Physical Education', 'experience': '10 years'})
school.add_teacher({'id': 2, 'name': 'Ms. Green', 'subject': 'Music', 'experience': '8 years'})

# Viewing teachers
school.view_teachers()

# Updating teacher details
school.update_teacher(1, {'experience': '12 years'})

# Deleting a teacher
school.delete_teacher(2)
