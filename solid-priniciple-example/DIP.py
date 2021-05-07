"""
Dependency Inversion Principle
Dependency should be on abstractions not concretions
A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
B. Abstractions should not depend on details. Details should depend upon abstractions.
There comes a point in software development where our app will be largely composed of modules.
When this happens, we have to clear things up by using dependency injection.
High-level components depending on low-level components to function.
"""

from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
    PARENT  = 0
    CHILD   = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self): pass


class Relationships(RelationshipBrowser): # Low -level
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child ))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                yield r[2].name
        pass


class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type
    # Hence we moved storage dependent method in relationship to avoid such issue as per DIP Principles

    # def __init__(self, relationships):
    #
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'{r[0].name} has children : {r[2].name}')

    def __init__(self, relationships):

        for p in relationships.find_all_children_of("John"):
            print(f'John has a child called {p}')



parent = Person('John')
child1 = Person('Chris')
child2 = Person('Hinson')


rel = Relationships()
rel.add_parent_and_child(parent, child1)
rel.add_parent_and_child(parent, child2)

Research(rel)
