students=[{"Name":"Crystal","Age":21,"Grades":{"English":90,"Science":97,"SST":90,"Math":70}}]
import json
import os

def save_students():
    if not os.path.exists("student_record.json"):
        with open("student_record.json","w") as file:
            json.dump(students,file,indent=4)
save_students()


def main_menu():
    print("1. View students")
    print("2. Enter new students")
    print("3. Update student data")
    print("4. Exit")
    choose()

def choose():
    number=input("Enter a number to act.")
    if number=="1":
        view_students()
    elif number=="2":
        entering_many()
    elif number=="3":
        update_student()
    elif number=="4":
        print("Goodbye")
    else:
        print("Make a valid entry")

def load():
    with open("student_record.json","r") as file:
        return json.load(file)

def enter_student():
    new_student={}
    new_student["Name"]=input("What is your name?")
    new_student["Age"] = input("How old are you?")
    print("Please enter your grades in the following subjects;")
    new_student["Grades"]={"English":input("English: "),
                           "Science":input("Science: "),
                           "SST": input("SST: ")
                           ,"Math":input("Math: ")}
    with open("student_record.json","r+") as file:
        loaded_data=json.load(file)
        loaded_data.append(new_student)
        file.seek(0)
        json.dump(loaded_data,file,indent=4)
        print(f"Data on {new_student["Name"]} has been saved!")

def view_students():
    with open("student_record.json","r") as file:
        loaded=json.load(file)
        print(json.dumps(loaded, indent=4))
        main_menu()

def entering_many():
    while True:
        choice=input("Enter another student? (y/n)")
        if choice=="y":
            enter_student()
        elif choice=="n":
            main_menu()
            break
        else:
            print("Make a valid entry!")

def update_student():
    students=load()
    update=input("Please enter a student whose data you want to edit.")
    for student in students:
        if student["Name"].lower()==update.lower():
            student["Name"]=input(f"Enter a new name. (Current:{student["Name"]})")
            student["Age"] = int(input(f"Enter a new age. (Current:{student["Age"]})"))
            print("Enter new grades for the subjects")
            student["Grades"]["English"] = int(input(f"English(Current:{student["Grades"]["English"]}): "))
            student["Grades"]["Science"] = int(input(f"Science(Current:{student["Grades"]["Science"]}): "))
            student["Grades"]["SST"] = int(input(f"SST(Current:{student["Grades"]["SST"]}): "))
            student["Grades"]["Math"] = int(input(f"Math(Current:{student["Grades"]["Math"]}): "))
            with open("student_record.json","w") as file:
                json.dump(students,file,indent=4)
                print(f"Data on {student["Name"]} has been saved successfully!")
                view_students()
            break
        else:
            print("Sorry this student does not exist")




print("WELCOME TO THE STUDENT INFORMATION CENTRE")
main_menu()