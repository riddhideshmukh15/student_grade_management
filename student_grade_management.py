student_grades={  }
def add_student(name,grade):
    student_grades[name]=grade
    print(f"added {name} with a {grade}")

def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name}is not found")
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been sussesfully deleted ")
    else:
        print(f"{name}is not found")
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
          print(f"{name} : {grade}")
    else:
        print("no students found")
def main():
    while True:
        print("\n students grades management system" ) 
        print("1.add student")
        print("2.update student")
        print("3.delete student")
        print("4.view student")
        print("5.exit")
        choice=int(input("enter the choice"))
        if choice==1:
           name=input("enter the student name")
           grade=int(input("enter student grades"))
           add_student(name,grade)
        elif choice==2:
          name=input("enter the student name")
          grade=int(input("enter student grades"))
          update_student(name,grade)
        elif choice==3:
          name=input("enter the student name")
          delete_student(name)
        elif choice==4:
          display_all_students()
        elif choice==5:
           print("closing the program")
           break
        else:
           print("invalid choice")
main()      

