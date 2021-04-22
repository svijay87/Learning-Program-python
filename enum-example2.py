from enum import Enum

class Mood(Enum):

    funky = 1
    happy = 3

    def describe(self):
        return self.name, self.value

    def __str__(self):
        return f'my custom str! {self.value}'

    @classmethod
    def favorite_mood(cls):
        return cls.happy



print(Mood.favorite_mood())
print(Mood.happy.describe())

print(str(Mood.funky))

# Subclassing an enumeration is allowed only if the enumeration does not define any members. So this is forbidden:

class Color(Enum):
    red = 1
    green = 2
    black = 3

# class MoreColor(Color):
#     # Throw error TypeError: MoreColor: cannot extend enumeration 'Color'
#     pink = 4

# However below case is allowed

class Foo(Enum):
    def some_behaviour(self):
        pass

class Bar(Foo):
    happy = 1
    sad = 2

from test.test_enum import Fruit
from pickle import loads, dumps

# print(Fruit.tomato is loads(dumps(Fruit.tomato)))

# Functional API

Animal = Enum('Animal', 'ant bee cat dog')

print(Animal)
print(Animal.ant)

print(list(Animal))
#Enum signiture
# Enum(value='NewEnumName', names=<...>, *, module='...', qualname='...', type=<mixed-in class>)