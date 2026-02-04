# -------------------------------
# Student Academic Analytics
# -------------------------------

class Student:
    def __init__(self, student_id, department):
        self.student_id = student_id
        self.department = department
        self.courses = []
        self.gpa = 0.0

    def add_course(self, course_name, score, credit_unit):
        self.courses.append((course_name, score, credit_unit))

    def score_to_gp(self, score):
        if score >= 70:
            return 5
        elif score >= 60:
            return 4
        elif score >= 50:
            return 3
        elif score >= 45:
            return 2
        elif score >= 40:
            return 1
        else:
            return 0

    def calculate_gpa(self):
        total_points = 0
        total_credits = 0

        for course, score, credit in self.courses:
            gp = self.score_to_gp(score)
            total_points += gp * credit
            total_credits += credit

        if total_credits > 0:
            self.gpa = total_points / total_credits
        else:
            self.gpa = 0


# -------------------------------
# CREATE STUDENTS
# -------------------------------

student1 = Student("KUST001", "Computer Science")
student1.add_course("Programming", 75, 3)
student1.add_course("Mathematics", 65, 2)
student1.calculate_gpa()

student2 = Student("KUST002", "Computer Science")
student2.add_course("Programming", 45, 3)
student2.add_course("Mathematics", 50, 2)
student2.calculate_gpa()

students = [student1, student2]


# -------------------------------
# PRINT OUTPUT
# -------------------------------

print("\n--- STUDENT RESULTS ---")
for s in students:
    print(f"ID: {s.student_id}")
    print(f"Department: {s.department}")
    print(f"GPA: {s.gpa:.2f}")
    print("-" * 30)


# -------------------------------
# AT-RISK STUDENTS
# -------------------------------

print("\n--- AT-RISK STUDENTS (GPA < 2.0) ---")
for s in students:
    if s.gpa < 2.0:
        print(s.student_id)


# -------------------------------
# SAVE REPORT TO FILE
# -------------------------------

with open("report.txt", "w") as file:
    file.write("STUDENT ID | DEPARTMENT | GPA\n")
    file.write("-" * 30 + "\n")
    for s in students:
        file.write(f"{s.student_id} | {s.department} | {s.gpa:.2f}\n")