class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Person: Name - {self.name}, Age - {self.age}")


class Student(Person):
    def _init_(self, name, age, student_id):
        super()._init_(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


class LibraryMember(Student):
    def _init_(self, name, age, student_id, library_card_number):
        super()._init_(name, age, student_id)
        self.library_card_number = library_card_number

    def display_info(self):
        super().display_info()
        print(f"Library Card Number: {self.library_card_number}")


# Demonstration with user input
name = input("Enter name: ")
age = int(input("Enter age: "))
student_id = input("Enter student ID: ")
library_card_number = input("Enter library card number: ")

library_member = LibraryMember(name, age, student_id, library_card_number)
library_member.display_info()
