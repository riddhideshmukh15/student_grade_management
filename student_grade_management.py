student_grades = {}

def add_student(name, grade):
    name = name.strip().lower()
    student_grades[name] = grade
    print(f"added {name} with a {grade}")


def update_student(name, grade):
    name = name.strip().lower()
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found")


def delete_student(name):
    name = name.strip().lower()
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found")


def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("no students found")


def search_student(name):
    name = name.strip().lower()
    if name in student_grades:
        print(f"{name}'s marks are {student_grades[name]}")
    else:
        print("student not found")


def main():
    while True:
        print("\nstudents grades management system")
        print("1.add student")
        print("2.update student")
        print("3.delete student")
        print("4.view student")
        print("5.search student")
        print("6.exit")

        try:
            choice = int(input("enter the choice: "))
        except ValueError:
            print("Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            name = input("enter the student name: ")
            grade = int(input("enter student grades: "))
            add_student(name, grade)

        elif choice == 2:
            name = input("enter the student name: ")
            grade = int(input("enter student grades: "))
            update_student(name, grade)

        elif choice == 3:
            name = input("enter the student name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            name = input("enter student name: ")
            search_student(name)

        elif choice == 6:
            print("program is closing")
            break

        else:
            print("invalid choice")


main()