import json
import os
data={"students":[{"Name":"Zoe","Age":24,"Grade":"A"},
                  {"Name":"Zayne","Age":25,"Grade":"B"},
                  {"Name":"Freya","Age":32,"Grade":"A+"}]}

def save():
    with open("student_data.json","w") as file:
        json.dump(data,file,indent=4)

def load():
    global data
    if os.path.exists("student_data.json"):
        with open("student_data.json","r") as file:
            data=json.load(file)
    else:
        save()

def display():
    for student in data["students"]:
        print("_"*40)
        print(f"Name: {student["Name"]}\n"
              f"Age: {student["Age"]}\n"
              f"Grade: {student["Grade"]}")


def new_entry():
    name=input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    new_student={"Name":name,"Age":age,"Grade":grade}
    data["students"].append(new_student)
    save()
def main_menu():
    load()
    print("Welcome to the school management student!")
    print("1. View students\n"
          "2. Enter new student\n"
          "3. Update student data\n"
          "4. Exit")
    choice=input("Enter the number for what you want to do: ")
    if choice=="1":
        display()
        main_menu()
    elif choice=="2":
        while True:
            new_entry()
            repeat=input("Do you want to enter another student(y/n)? ")
            if repeat=="n":
                break
            elif repeat!="y":
                print("Invalid entry! Please enter y or n.")
        display()
        main_menu()

    elif choice=="3":
        update()
    elif choice=="4":
        print("Goodbye!")
    else:
        print("Make a valid entry")

def update():
    load()
    display()
    updated_student = input("Enter a student whose details yo want to update")
    for student in data["students"]:
        if student["Name"].lower()==updated_student.lower():
            student["Name"]=input(f"Enter {student["Name"]}'s new name. Current:{student["Name"]}: ")
            student["Age"] = input(f"Enter {student["Name"]}'s new age. Current:{student["Age"]}: ")
            student["Grade"] = input(f"Enter {student["Name"]}'s new grade. Current:{student["Grade"]}: ")
            save()
            print(f"\n{updated_student}'s data updated successfully")
            print("Updated student list!")
            display()

main_menu()
