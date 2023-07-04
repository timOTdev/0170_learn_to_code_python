# Source - https://learnxinyminutes.com/docs/python/

####################################################
## 1. Primitive Datatypes and Operators
####################################################

# Single line comment
# This is a single line comment.

# Multiple line comment
"""
	Hello world.
	Hello universe.
"""

# Booleans (capitalization!)
True == True
False != True

# True and False are actually 1 and 0 but with different keywords
True + True # => 2
True * 8    # => 8
False - 5   # => -5

# Equality is ==, Inequality is !=
1 == 1  # => True
1 != 1  # => False

# Integer division rounds down for both positive and negative numbers.
5 // 3       # => 1
-5 // 3      # => -2
5.0 // 3.0   # => 1.0 # works on floats too
-5.0 // 3.0  # => -2.0

# Exponentiation (x**y, x to the yth power)
2**3  # => 8

# You can also format using f-strings or formatted string literals (in Python 3.6+)
# Like JavaScript's template literals
name = "Reiko"
f"{name} is {len(name)} characters long." # => "Reiko is 5 characters long."

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too
"Hello " + "world!"  # => "Hello world!"

# None is an object
None  # => None

####################################################
## 2. Variables and Collections
####################################################

# Python has a print function
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

# Simple way to get input data from console
input_string_var = input("Enter some data: ") # Returns the data as a string

# Ternary operator
"yay!" if 0 > 1 else "nay!"  # => "nay!"

# Lists
li = []
other_li = [4, 5, 6]
li.append(1)    # li is now [1]
li.append(2)    # li is now [1, 2]
li.append(4)    # li is now [1, 2, 4]
li.append(3)    # li is now [1, 2, 4, 3]
li.pop()        # => 3 and li is now [1, 2, 4]
li[0]   # => 1
li[-1]  # => 3
li[4]  # Raises an IndexError
# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
li[1:3]   # Return list from index 1 to 3 => [2, 4]
li[2:]    # Return list starting from index 2 => [4, 3]
li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
li[::2]   # Return list selecting every second entry => [1, 4]
li[::-1]  # Return list in reverse order => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Check for existence in a list with "in"
# Use in lists, tuples, and dictionaries
# Like C#'s .contains or JS's .includes
1 in li  # => True

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True
# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4

# Dictionaries store mappings from keys to values
# Note keys for dictionaries have to be immutable types for quick look-ups.
# as of Python 3.7, dictionary items maintain the order at which they are inserted into the dictionary.
# Immutable types include ints, floats, strings, tuples
empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}

# The get method supports a default argument when the value is missing
filled_dict.get("one", 4)   # => 1

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5

# Sets. Looks similar to dictionaries.
# Like Javascript Sets without the comparison features.
empty_set = set()
some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1, 2, 3, 4}

# Sets do not have duplicate elements
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
filled_set.add(5)  # it remains as before {1, 2, 3, 4, 5}

# Set intersection with &
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Set union with |
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Set difference with -
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Set symmetric difference with ^
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}

# Make a one layer deep copy
filled_set = some_set.copy()  # filled_set is {1, 2, 3, 4, 5}

####################################################
## 3. Control Flow and Iterables
####################################################
animals = ["dog", "cat", "mouse"]

# For loops iterate over lists
"""
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in animals:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))
		
# To loop over a list, and retrieve both the index and the value of each item in the list
"""
prints:
    0 dog
    1 cat
    2 mouse
"""
for i, value in enumerate(animals):
    print(i, value)
		
# While loops
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1
		
# Writing to a file
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))        # writes a string to a file

with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents)) # writes an object to a file

# Reading from a file
with open('myfile1.txt', "r+") as file:
    contents = file.read()           # reads a string from a file
print(contents)
# print: {"aa": 12, "bb": 21}

with open('myfile2.txt', "r+") as file:
    contents = json.load(file)       # reads a json object from a file
print(contents)
# print: {"aa": 12, "bb": 21}

# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned by the range function, is an iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three']). This is an object that implements our Iterable interface.

# However we cannot address elements by index.
our_iterable[1]  # Raises a TypeError

# We can loop over it.
for i in our_iterable:
    print(i)  # Prints one, two, three
		
# Our iterator is an object that can remember the state as we traverse through it.
# We get the next object with "next()".
# Like JavaScript generators.
next(our_iterator)  # => "one"

####################################################
## 4. Functions
####################################################

# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement

# Calling functions with parameters
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
add(y=6, x=5)  # Keyword arguments can arrive in any order.

# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

####################################################
## 5. Modules
####################################################

# You can import modules
# import math
# from math import * (Not recommended to import all functions from a module)
# import math as m (You can shorten module names)
# specific functions from a module
import math
from math import ceil, floor
print(math.sqrt(16))  # => 4.0
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

# Python modules are just ordinary Python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.
# You can find out which functions and attributes
# are defined in a module.
dir(math)

# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries.

####################################################
## 6. Classes
## 6.1 Inheritance
## 6.2 Multiple Inheritance
## 7. Advanced
####################################################
# Too much to cover here, visit LearnX - https://learnxinyminutes.com/docs/python/
# Briefly, classes have:
	# Initializer - called when class is instantiated. Like JS constructor.	
	# Class attributes - property shared by all instances of class.
	# Class methods - method shared among all instances. Use @classmethod.
	# Instance methods - all methods takes "self" as first argument.
	# Static methods - called without class or instance reference. Use @staticmethod.
	# Property - Makes easy getters and setters. Use @property, @[property].setter, @[property].deleter.
	# pass - inherit all of the parent's definitions without any modification
	# super() - The "super" function lets you access the parent class's methods that are overridden by the child
	
	# Generators are memory-efficient because they only load the data needed to process the next value in the iterable
	# Decorators are design patterns in Python that allows a user to add new functionality to an existing object without modifying its structure
	# Decorators in Python can use @decorator path instead of having to write closures.
	# If using multiple decorators, the application is from the bottom and goes up. @uppercase_decorator before @split_string
	# Source: https://www.datacamp.com/community/tutorials/decorators-python
	@split_string
	@uppercase_decorator
	def say_hi():
			return 'hello there'
	say_hi()