from enum import Enum, unique

# Having two enum members with the same name is invalid:
# Class Shape(Enum):
#    square = 2
#    square = 3
# TypeError: Attempted to reuse key: 'square'

# However, two enum members are allowed to have the same value. Given two members A and B with the same value (and A defined first),
# B is an alias to A. By-value lookup of the value of A and B will return A. By-name lookup of B will also return A:
class Shape(Enum):
    square = 2
    alias_for_square = 2
    diamond = 1
    circle = 3

print(list(Shape))

# The special attribute __members__ is an ordered dictionary mapping names to members.
# It includes all names defined in the enumeration, including the aliases:

for name, member in Shape.__members__.items():
    print(f'{name} => {member}')


# Enumeration members are compared by identity:
print(f'\nCOMPARISON by identity :: {Shape.square is Shape.diamond} \n')
print(f'COMPARISON by identity :: {Shape.square is Shape.alias_for_square} \n')
print(f'COMPARISON by identity :: {Shape.square == Shape.alias_for_square} \n')

print('Now checking alias scenario')
print(Shape.square)
print(Shape.alias_for_square)
print(Shape(2))

# Ensure Unique enumration values

@unique
class Mistake(Enum):
    one = 1
    two = 2
    three = 3
    # four = 3

# It will return ValueError: duplicate values found in <enum 'Mistake'>: four -> three


class ArmForces(Enum):
    Army = 1
    Navy = 2
    AirForce = 3


# print(ArmForces.Army)
# print(ArmForces.AirForce)
print(ArmForces(3))
print(ArmForces['Navy'].name)
print(ArmForces['Navy'].value)

for forces in ArmForces:
    print(f'Force Name {forces.name} => Value {forces.value}')


