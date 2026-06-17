class car:
    def __init__(self,brand):
        self.brand = brand
    def drive(self):
        print(self.brand,"is driving")
car1=car("Toyota")
car1.drive()

class student:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age
    def info(self):
        print("Student name: "+str(self.name))
        print("Student grade: "+str(self.grade))
        print("Student age: "+str(self.age))
student1=student("Yuv",9,13)
student2=student("Mark",8,12)
student1.info()
student2.info()
#Notes: A class is like a blueprint. Init for initialising and assigning attributes as soon as the object is created.
#Notes: Functions can use these attributes.
class fruit:
    def __init__(self,name,colour,size):
        self.colour = colour
        self.size = size
        self.name = name
    def taste_facts(self):
        print(str(self.name)+" is "+str(self.colour)+" and is "+str(self.size)+" sized.")
        print(str(self.name)+" is/are tasty!")
fruit1=fruit("Banana","yellow","medium")
fruit1.taste_facts()