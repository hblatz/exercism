https://realpython.com/python-tuple/
# all tuples require a comma.
# single tuples still require a comma.
one_number = (42,)

# creating a tuple using literals

# Python assumes that a comma separated list is a tuple:
# >>> item_0, item_1, ..., item_n  <-- n-tuple
three_items = "hook", "line", "sinker"
three_items
# ('hook', 'line', 'sinker')

# round parethases, (), are used to declare tuples.
jane = ("Jane Doe", 25, 1.75, "Canada")
jane
# ('Jane Doe', 25, 1.75, 'Canada')

# creating tuples with the tuple() constructor
jane = tuple(["Jane Doe", 25, 1.75, "Canada"])
jane
# ("Jane Doe", 25, 1.75, "Canada")

# the list literals square brackets, [], tell Python to iterate with items between commas.
jane = tuple(["Jane Doe",])
# >>> jane
# ('Jane Doe',)
jane = tuple("Jane Doe",)
jane
# ('J', 'a', 'n', 'e', ' ', 'D', 'o', 'e')

# Accessing nested tuples:
employee = ("John",35,"Python Developer", ("Django", "Flask", "FastAPI", "CSS", "HTML"),)
skill_2 = employee[3][2]
skill_2
# 'FastAPI'

# tuples can be sliced --> item[start:end:step]
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
mwf = days[:5:2]
mwf
# ('Monday', 'Wednesday', 'Friday')

# tuples do NOT have .append(), .extend(), .insert(), .remove(), and .clear() methods
# and you can NOT delete, del, an element of a tuple. 

# You can change a mutable object embedded in a tuple:
student_info = ("Linda", 18, ["Math", "Physics", "History"])
student_info[2][2] = "Engineering" # changes the 3rd list itme in the tuple's 3rd item.
student_info
# ('Linda', 22, ['Math', 'Physics', 'Engineering'])

# Tuples can be keys in a dictionary if none of its elements are mutable.
# The keys must be hashable, meaning an index based on content never changes.
student_courses = {("John", "Doe"): ["Physics", "Chemistry"],
                   ("Jane", "Doe"): ["English", "History"],}
student_courses[("Jane", "Doe")]
# ['English', 'History']
student_courses = {["John", "Doe"]: ["Physics", "Chemistry"],
                   ["Jane", "Doe"]: ["English", "History"],}
# >>> TypeError: unhashable type: 'list'

# Tuples can be unpacking:
three_d_point = (7, 14, 21)
x_axis, y_axis, z_axis = three_d_point
# >>> y_axis
# 14

numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
middle
# [2, 3, 4]
first, second, *rest = numbers
# >>> rest
# [3, 4, 5]
_, second, *_ = numbers
second
# 2

# Merging tuples
name = ("John", "Doe")
contact = ("john@example.com", "55-555-5555")
merged_record = (*name, *contact)
merged_record
# ('John', 'Doe', 'john@example.com', '55-555-5555')


# Return a tuple from a function
def find_extremes(iterable):
    data = tuple(iterable)
    if len(data) == 0:
        raise ValueError("input iterable must not be empty")
    return min(data), max(data)  # Python assumes a tuple.

find_extremes([3, 4, 9, 6, 7, 1, 2])
# (1, 9)

# Since tuples are imutable, Python doesn't make copies of tuples for slices and copies as it does with lists.
# For slices and copies, Python references the original tuple. You can confirm this with id().
student_info = ("Linda", 18, ["Math", "Physics", "History"])
student_profile = student_info[:]
id(student_info) == id(student_profile)
# True  # the object ids are identical. 
from copy import copy
student_profile_2 = copy(student_info)
id(student_info) == id(student_profile_2)
# True

# IMPORTANT -- If you change a mutable object in an element of one instance of the tuple
# then all aliases / instances are also changed. 


#Concatinating a tuple with other tuples by using the plus sign, +:
personal_info = ("John", 35)
professional_info = ("Computer science", ("Python", "Django", "Flask"))

profile = personal_info + professional_info
profile
# ('John', 35, 'Computer science', ('Python', 'Django', 'Flask'))

# When using the augmented concatination, +=, a new tuple is created.
profile = ("John", 35)
id(profile)
# 4420700928
profile += ("Computer science", ("Python", "Django", "Flask"))  # += reasigns tuple name but to a new tuple.
id(profile)
# 4406635200
profile
# ('John', 35, 'Computer science', ('Python', 'Django', 'Flask'))

# Repeating tuples
numbers = (1, 2)
numbers * 3
# (1, 2, 1, 2, 1, 2)
3 * numbers
# (1, 2, 1, 2, 1, 2)

numbers = (1, 2)
numbers *= 3  # *= reasigns tuple name but to a new tuple.
numbers
# (1, 2, 1, 2, 1, 2)

# built-in reversed() and sorted() methods
vowels = ("a","e","i","o","u")
reversed(vowels)
# <reversed object at 0x0000026D82015570>
tuple(reversed(vowels))
# ('u', 'o', 'i', 'e', 'a')
# Reversing can also be done with a slice and stepping backwards:
vowels[::-1]

# Sorted()
numbers = (2, 9, 5, 1, 6)
sorted(numbers)
# [1, 2, 5, 6, 9]  # Notice that a list is returned.

# Sorting in verse order - use key word, reverse=True
Sorted(numbers, reverse=True)
# [9, 6, 5, 2, 1]

https://realpython.com/python-tuple/#traversing-tuples-in-python


monthly_incomes = (("January", 5000),
                   ("February", 5500),
                   ("March", 6000),
                   ("April", 5800),
                   ("May", 6200),
                   ("June", 7000),
                   ("July", 7500),
                   ("August", 7300),
                   ("September", 6800),
                   ("October", 6500),
                   ("November", 6000),
                   ("December", 5500)
                   )

def annual_statement(monthly_incomes):
    quarter_income = 0
    total_income = 0
    for index, (month, income) in enumerate(monthly_incomes, start=1):  # creates nested tuples: (index, (month, income))
        print(f"{month:>10}: {income}")  # right justifies month to 10th position, then prints a colon and then income
        quarter_income += income  # totals the monthly incomes to be reset in the following if-statement after 3rd month
        if index % 3 == 0:
            print("-" * 20)  # prints a line of 20 dashes
            print(f"{'Quarter':>10}: {quarter_income}", end="\n\n")  # right justifies the quarter label, adds to newlines.
            total_income += quarter_income
            quarter_income = 0
    print("=" * 20)
    print(f"{'Annual':>10}: {total_income}", end="\n\n")


# List Comprehensions and Generator Expressions
# Comprehension: 
numbs_as_str = ("2", "9", "5", "1", "6")  # numbers as strings in tuple
# iterate num_str through numbs_as_str and return integers in a list that is converted to a tuple. 
tuple([int(num_str) for num_str in numbs_as_str])
# (2, 9, 5, 1, 6)

# Generator expression:
tuple(int(num_str) for num_str in numbs_as_str)


# Tuples have two methods: .count() and .index()
# Use .count() to count the number of occurrences of an item in a tuple.
fruits = ("apple", "banana", "orange", "apple", "apple", "kiwi", "banana")
fruits.count("apple")
# 3
# .index() finds the location of the first instance.
fruits.index("banana")  # zero-based indexing
# 1

# Use 'in' or 'not in' to test membership in a collection. 
"kiwi" in fruits
# True

# Note that membership tests use search algorithms and slow as the collection grows. 
https://wiki.python.org/moin/TimeComplexity

# Sets are more efficient than large collections.

# Length of a tuple.
# len() returns the number of items in the tuple.
employee = ("John Doe", "Python Developer", "Remote", "Canada")

len(employee)   
# 4

# Comparisons:
# Python uses lexicographical ordering:
https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types
# Python compares the first two elements, then the next two, etc.
(1, 2, 3) < (1, 2, 4)
# True

# Common Gotchas of Python Tuples:

# 1
# forgetting the trailing comma.
numbers = (42)  # Oops! No comma, so defined as in int() instead of a tuple(,)

numbers.index(42)
# Traceback (most recent call last):
#    ...
# AttributeError: 'int' object has no attribute 'index'

# 2
# Including a non-hashable element in a tuple to be used as an key.
# This cities and population dictionary has coordinates in a list as part of the key: 
cities = {("Vancouver", [49.2827, -123.1207]): 631_486, ("Denver", [39.7392, -104.9903]): 716_492}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'


# tuples with names for fields instead of index numbers:
https://realpython.com/python-namedtuple/
# use the namedtuple() built-in function from the collections module:
from collections import namedtuple
# define a class and name its fields
Person = namedtuple("Person", "name age position")  # define class, 'Person' with fields: name, age, position
# use the class
person = Person("John", 35, "Python Developer")
person.name
# 'John'

# example using the built-in divmod() function, which returns a tuple of quotient and remainder as index 0 and index 1
from collections import namedtuple

def custom_divmod(a, b):
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(a, b))

custom_divmod(8, 3)
# DivMod(quotient=2, remainder=2)


# Tuples With Named Fields and Type:
# Python 3.5 introduced a module called typing to support type hints. 
# This module exports the NamedTuple class, which is a typed version of namedtuple. 
# With NamedTuple, you can create tuple subclasses with type hints and default values.

# Example:
# CSV file named employees.csv
"""name,age,position
"Fatima",28,"Technical Lead"
"Joe",32,"Senior Web Developer"
"Lara",40,"Project Manager"
"Miguel",25,"Data Analyst"
"Jane",40,"Senior Python Developer"
"""

from typing import NamedTuple   # the NamedTuple class allows for setting data types.

class Employee(NamedTuple):     # defines the supclass Employee()
    name: str                           # sets data types
    age: int
    position: str = "Python Developer"  # sets a default value.

import csv

with open("C:/Users/huntb/OneDrive/Documents/GitHub/exercism/python_exercises/01_employees.csv", mode="r") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip headers
    employees = []
    for name, age, position in reader:
        employees.append(Employee(name, int(age), position))

""" First, import the csv module to manipulate the CSV file. 
In the with statement, open employees.csv for reading. 
Use reader() to load the file content. 
Call to the built-in next() function to skip the first line.

The for loop iterates over the rest of the rows in the CSV file and appends 
them to a list of employees. 
To create a record for each employee, use the Employee class with the data 
for each field as arguments. 
Note: use the built-in int() function to convert the age to an 
integer value and make it type-consistent."""
employees
# [Employee(name='Fatima', age=28, position='Technical Lead'), 
#  Employee(name='Joe', age=32, position='Senior Web Developer'), E
#  mployee(name='Lara', age=40, position='Project Manager'), 
#  Employee(name='Miguel', age=25, position='Data Analyst'), 
#  Employee(name='Jane', age=40, position='Senior Python Developer')] 

# Data Classes: dataclasses.dataclass
# Python 3.7 added data classes to the standard library.
# Similar to named tuples but mutable by default.
# Use data classes to replace your named tuples with a more powerful tool including: 
#   having type hints, default attribute values, methods, etc. 
#   and capable  of becoming immutable.
https://realpython.com/python-data-classes/

# Use the @dataclass decorator from dataclasses to create a data class.
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    position: str = "Python Developer"

# Similar to the NamedTuple version.
# Instead of inheriting from another class, use the @dataclass decorator, 
# imported from the dataclasses module.

# This dataclass version of Employee works the same as the NamedTuple version.

# These records are mutable by default.
# To make immutable, pass the frozen argument to the @dataclass decorator in the definition.

@dataclass(frozen=True)  # frozen=True makes the data class immutable. 
class Employee:
    name: str
    age: int
    position: str = "Python Developer"

