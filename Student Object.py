import StudentClass as sc


def main():
    sID = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = int("Enter student date of birth (MM/DD/YYYY): ")
    classif = "Enter student classification (F,S,Jr,Sr): "

    student_1 = sc.Student(sID, name, dob, classif)
