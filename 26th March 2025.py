class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"Hello\n"
              f"My name is {self.name} and I am {self.age} years old!")

class employee(person):
    def __init__(self,name,age,job_title,department):
        super().__init__(name, age)
        self.job_title=job_title
        self.department=department

class manager(employee):
    def __init__(self,name,age,job_title):
        super().__init__(name,age,job_title)
    def introduce(self):
        print(f"Hey, I'm {self.name} and I'm a {self.age} year old {self.job_title}")


emp_1=employee("Janet",45,"Secretary")
emp_1.introduce()
emp_2=manager("Yusuf",33,"General manager")
emp_2.introduce()

class vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def description(self):
        print(f"The vehicle is {self.make}, {self.model}.")
class car(vehicle):
    def __init__(self,make,model,doors):
        super().__init__(make,model)
        self.doors=doors

car_1=car("Mercedes","S-class",5)
car_1.description()