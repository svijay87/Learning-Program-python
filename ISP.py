"""
Interface Segregation Principle
Make fine grained interfaces that are client specific
Clients should not be forced to depend upon interfaces that they do not use.
This principle deals with the disadvantages of implementing big interfaces.
"""


class IShape:
    def draw(self):
        raise NotImplementedError


class Circle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass


class Rectangle(IShape):
    def draw(self):
        pass