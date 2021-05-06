# Single Responsibility Principle Example
# SRP Should server single responsiblity

"""
SRP states that classes should have one responsibility, here, we can draw out two responsibilities: animal database
management and animal properties management. The constructor and get_name manage the Animal properties while the save
manages the Animal storage on a database.
How will this design cause issues in the future?
If the application changes in a way that it affects database management functions. The classes that make use of Animal
properties will have to be touched and recompiled to compensate for the new changes.

...............
When designing our classes, we should aim to put related features together,
so whenever they tend to change they change for the same reason.
And we should try to separate features if they will change for different reasons. - Steve Fenton
"""

class Animal:
    def __init__(self : object, name : str = 'Tiger') -> None:
        self.name = name

    def get_name(self : object) -> str:
        return self.name


class Animal_Update:
    def update_animal(self, animal : Animal):
        pass