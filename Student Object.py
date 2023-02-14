import StudentClass as sc


def main():
    sID = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (MM/DD/YYYY): ")
    classif = input("Enter student classification (F,S,Jr,Sr): ")

    student_1 = sc.Student(sID, name, dob, classif)

    student_1.age_calc()

    student_1.register()

    print("Student age is:", student_1.get_age())

    print("Student can reigster between:", student_1.return_registration())
