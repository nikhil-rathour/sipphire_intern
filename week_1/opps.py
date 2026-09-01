# 5. OOPS - Object-Oriented Programming is a programming approach based on Classes and Objects.


# 5.1 Class - A class is a blueprint for creating objects.

class Student:

    name = "Nikhil"
    age = 21
    course = "Python"


# 5.2 Object - An object is an instance of a class.

student1 = Student()

print(f"name = {student1.name}")
print(f"age = {student1.age}")
print(f"course = {student1.course}")



# 5.3 Constructor - __init__() is a special method that is automatically called
# when an object is created.

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student1 = Student("Nikhil", 21, "Python")

print(f"name = {student1.name}")
print(f"age = {student1.age}")
print(f"course = {student1.course}")


# 5.4 Method - A method is a function defined inside a class.

class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


student1 = Student("Nikhil")

student1.introduce()


# 5.5 Encapsulation - Encapsulation means combining data and methods
# inside a class and controlling access to the data.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(f"Balance = {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount


account = BankAccount(5000)

account.deposit(2000)
account.show_balance()


# 5.6 Inheritance - Inheritance allows one class to use properties and methods
# of another class.

class Animal:

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()
dog.bark()


# 5.7 Multiple Inheritance - A class can inherit from more than one class.

class Father:

    def father_property(self):
        print("Father property")


class Mother:

    def mother_property(self):
        print("Mother property")


class Child(Father, Mother):

    def child_property(self):
        print("Child property")


child = Child()

child.father_property()
child.mother_property()
child.child_property()


# 5.8 Polymorphism - Polymorphism means the same method name can have
# different behavior in different classes.

class Dog:

    def sound(self):
        print("Woof")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# 5.9 Method Overriding - A child class can provide its own implementation
# of a method that already exists in the parent class.

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()


# 5.10 Abstraction - Abstraction means hiding implementation details
# and showing only the required functionality.

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()


# 5.11 Class Variable - A variable that is shared by all objects of a class.

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name


student1 = Student("Nikhil")
student2 = Student("Rahul")

print(f"student1 school = {student1.school}")
print(f"student2 school = {student2.school}")


# 5.12 Instance Variable - A variable that belongs to a particular object.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Nikhil", 21)
student2 = Student("Rahul", 22)

print(f"student1 name = {student1.name}")
print(f"student1 age = {student1.age}")

print(f"student2 name = {student2.name}")
print(f"student2 age = {student2.age}")


# 5.13 self Keyword - self refers to the current object of the class.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")


student1 = Student("Nikhil", 21)

student1.display()


# 5.14 __str__() Method - Used to define how an object should be represented
# as a string.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"


student1 = Student("Nikhil", 21)

print(student1)


# 5.15 OOPS Four Main Principles
#
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction



