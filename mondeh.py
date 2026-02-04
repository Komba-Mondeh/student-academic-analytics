import tkinter as tk
from tkinter import ttk

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

        self.gpa = total_points / total_credits if total_credits > 0 else 0


# -------------------------------
# CREATE STUDENTS
# -------------------------------

student1 = Student("KUST001", "Computer Science")
student1.add_course("Programming", 75, 3)
student1.add_course("Mathematics", 65, 2)
student1.calculate_gpa()

student2 = Student("KUSTS002", "Computer Science")
student2.add_course("Programming", 45, 3)
student2.add_course("Mathematics", 50, 2)
student2.calculate_gpa()

students = [student1, student2]


# -------------------------------
# GUI FUNCTIONS
# -------------------------------

def load_students():
    table.delete(*table.get_children())

    for s in students:
        status = "AT RISK" if s.gpa < 2.0 else "OK"
        table.insert("", "end", values=(s.student_id, s.department, f"{s.gpa:.2f}", status))


# -------------------------------
# GUI SETUP
# -------------------------------

root = tk.Tk()
root.title("Student Academic Analytics System")
root.geometry("600x400")

title = tk.Label(root, text="Student Academic Analytics", font=("Arial", 16, "bold"))
title.pack(pady=10)

columns = ("Student ID", "Department", "GPA", "Status")
table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor="center")

table.pack(expand=True, fill="both", padx=10, pady=10)

load_btn = tk.Button(root, text="Load Student Results", command=load_students)
load_btn.pack(pady=10)

root.mainloop()