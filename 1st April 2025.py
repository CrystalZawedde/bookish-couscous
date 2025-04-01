from gettext import install

try:
    print(x)
except NameError:
    print("x cannot be defined")
except:
    print("Error")

try:
    print("Hello")
except:
    print("An error occurred")
else:
    print("Operation successful")

names = ["Grace","Polly","Matthew"]
for name in names:
    print(f"{name}, Welcome to the spa!")
names[1]="Elliot"
print(names)
names.append("Micheal")
for name in names:
    print(f"{name}, Welcome to the spa!")
names.insert(2,"Phillip")
for name in names:
    print(f"{name}, Welcome to the spa!")


