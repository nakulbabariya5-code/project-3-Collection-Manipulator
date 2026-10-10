students  = {}
subjects = ["maths","science","english","Computer","gujarati"]
print("Welcome to the student Data Organizer!")
while True:
    print("select an option:")
    print("1.add student")
    print("2.display all students")
    print("3.update students information")
    print("4.Delete student ")
    print("5.display all subjects offered")
    print("6. exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        student_id = int(input("enter student id:"))
        if student_id in students:
            print("student id already exists")
        else:
            Name = input("enter your name:")
            Age = int(input("enter your age:"))
            Grade = input("enter your Grade:")
            date_of_birth =input("enter your date of birth  (dd/mm/yyyy):")
            subjects_input = input("subjects offered (comma separated):")
            subjects_input = [subject.strip() for subject in subjects_input.split(" . ")]
            students[student_id] = {
                "Name": Name,
                "Age": Age,
                "Grade": Grade,
                "Date of Birth": date_of_birth,
                "Subjects": subjects_input
            }
            print("student added successfully")
    elif choice== 2:
        print("Display all students")
        if len(students) ==0:
            print(" no student found")
        else:
            for student_id, student_info in students.items():
                print(f"Student ID: {student_id}")
                print(f"Name: {student_info['Name']}")
                print(f"Age: {student_info['Age']}")
                print(f"Grade: {student_info['Grade']}")
                print(f"Date of Birth: {student_info['Date of Birth']}")
                print(f"Subjects: {', '.join(student_info['Subjects'])}")
    elif choice == 3:
        student_id = int(input("enter student id to update:"))
        if student_id not in students:
            print("student not found!")
        else:
            print("\n 1. update name")
            print("2.update name")
            print("2.update age")
            print("3.update  grade")
            print("4.update date of birth")
            print("5.update subjects")
            update_choice = int(input("enter your choise:"))
            if update_choice == 1:
                students[student_id]["Name"] = input("enter new name: ")
            elif update_choice == 2:
                students[student_id]["Age"] = int(input("enter new age: "))
            elif update_choice == 3:
                students[student_id]["Grade"] = input("enter new grade: ")
            elif update_choice == 4:
                students[student_id]["Date of Birth"] = input("enter new date of birth: ")
            elif update_choice == 5:
                subjects_input = input("subjects offered (comma separated): ")
                students[student_id]["Subjects"] = [subject.strip() for subject in subjects_input.split(",")]
            else:
                print("invalid choice")
    elif choice == 4:
        student_id = int(input("enter student_id to delete: "))
        if student_id in students:
            del students[student_id]
            print("student_id deleted successfully")
        else:
            print("student not found")
    elif choice == 5:
        print("Subjects offered:")
        for subject in subjects:
            print(f"- {subject}")
    elif choice == 6:
        print("Exiting the student data organizer.")
        break
    else:
        print("invalid choice")
    
                                  

