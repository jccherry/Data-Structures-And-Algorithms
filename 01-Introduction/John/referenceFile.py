#reference file so that i can remember syntax and stuff

#variable declarations
integer = 10
double = 10.0
string = "10"

#print (functions must use peren in python 3, not 2.7)
print(integer)
print(double)
print(string)

#if elif else (also cast variables)
if int(string) == integer:
    print("yes")

#take input (string) from user
name = input("¿Como se llama? -->")
print(name)

#compare strings just like regular variables

if name == "juan":
    print("doesEqual juan")
elif name != "jose":
    print("doesNotEqual jose")
elif name == "jose":
    print("doesEqual jose")
else:
    print("aye aye aye")


#function declarations

def factorial( int ):
    if int == 0:
        return 1
    elif int == 1:
        return 1
    elif int < 0:
        return "error: argument must be positive or 0"
    else:
        return int * factorial(int - 1)

print(factorial(10))

#loops

for i in range(1,10):
    print(i)

#Classes

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayAge(self):
        print(self.name, "is",self.age,"years old")

zoey = Dog("zoey", 10)
zoey.displayAge()

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

nevyn = Employee("Nevyn", 0)

nevyn.displayEmployee()
