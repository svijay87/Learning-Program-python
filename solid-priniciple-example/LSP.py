"""
Liskov Substitution Principle
A sub-class must be substitutable for its super-class.
The aim of this principle is to ascertain that a sub-class can assume the place of its super-class without errors.
If the code finds itself checking the type of class then, it must have violated this principle.
Let’s use our Animal example.
"""


class Person:

    def breakfast(self, diet_plan):
        pass

    def lunch(self, diet_plan):
        pass

    def dinner(self, diet_plan):
        pass


class Patient(Person):
    def breakfast(self, diet_plan):
        pass

    def lunch(self, diet_plan):
        pass

    def dinner(self, diet_plan):
        pass

