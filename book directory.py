import json
from textwrap import indent

book={"Title":"Atomic habits","Author":"James clear","Year published":"2020","Genres":["productivity","self help"],"is_available":True}

with open("book.json","w") as file:
    json.dump(book,file, indent=4)
try:
    with open("book.json","r") as file:
        print(json.load(file))
except FileNotFoundError:
    print("File not found.")
book["Year published"]="2024"
book["Genres"].append("Personal finance")
book["is_available"]=False
with open("book.json","w") as file:
    json.dump(book,file,indent=4)
with open("book.json","r") as file:
    print("Updated data: ")
    print(json.load(file))

#making a list of three books
books=[
    {"Title":"1984",
     "Author":"George Orwell",
     "Year published":"1991",
     "Genres":["dystopian","fiction"],
     "Is_available":True},{"Title":"First move",
     "Author":"Julian Chatterly",
     "Year published":"2008",
     "Genres":["strategy","finance"],
     "Is_available":False},
    {"Title":"Seek God",
     "Author":"George Bevere",
     "Year published":"1997",
     "Genres":["Christian","non-fiction"],
     "Is_available":True}
]
with open("library.json","w") as file1:
    json.dump(books,file1,indent=4)

def show_books():
    with open("library.json","r") as file1:
        loaded_books=json.load(file1)
        for book in loaded_books:
            print(f"{book["Title"]} by {book["Author"]} ({book ["Year published"]})")

    #to enter a new book
def add_new_book():
    new_book={}
    new_book["Title"]=input("Please enter a title: ")
    new_book["Author"] = input("Please enter an author: ")
    new_book["Year published"] = input("Please enter the year the book was published: ")
    new_book["Genre"]=input("Please enter the genres: ").split(",")
    new_book["Is available"] = input("Is the book available?(True or False")=="true"
    with open("library.json", "r+") as file1:
        loaded_books=json.load(file1)
        loaded_books.append(new_book)
        file1.seek(0)
        json.dump(loaded_books,file1,indent=4)
        print(f"{new_book["Title"]} saved successfully")

while True:
    choice=input("Enter a new book?")
    if choice=="yes":
        add_new_book()
    elif choice=="no":
        show_books()
        break
    else:
        print("Make a valid entry")



