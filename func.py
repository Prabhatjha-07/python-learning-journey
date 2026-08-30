# def hello(meet , name = 'you'):
#     return f'hi! {meet}{name}'
    


# for g in range(5):
#     # print(hello().upper())
#     print(hello('mj' , 'prabhat'))

def student(*args , **kwargs):
    print(args)
    print(kwargs)
    
courses = ['maths' , 'science' , 'english' , 'hindi']
info = {'name' : 'prabhat' , 'age' : 20}

student(*courses , **info)

# student('prabhat' , 'mj' , 'sachin' , name = 'prabhat' , age = 20)

# ============================================================
# PYTHON NOTES — *args, **kwargs, TYPE HINTS & PACKAGES
# ============================================================


# ============================================================
# 1. PARAMETER vs ARGUMENT
# ============================================================

# Parameter = variable written in the function definition.
# Argument  = actual value passed when calling the function.

def add(a, b):          # a, b = parameters
    return a + b

add(10, 20)             # 10, 20 = arguments


# ============================================================
# 2. *args
# ============================================================

# *args collects multiple POSITIONAL arguments.
# Inside the function, args is stored as a TUPLE.

def student(*args):
    print(args)

student("Maths", "Science", "English")

# Output:
# ('Maths', 'Science', 'English')


# ============================================================
# 3. **kwargs
# ============================================================

# **kwargs collects multiple KEYWORD arguments.
# Inside the function, kwargs is stored as a DICTIONARY.

def student(**kwargs):
    print(kwargs)

student(name="Prabhat", age=20)

# Output:
# {'name': 'Prabhat', 'age': 20}


# ============================================================
# 4. *args + **kwargs
# ============================================================

def student(*args, **kwargs):
    print(args)
    print(kwargs)

student("Maths", "Science", name="Prabhat", age=20)

# args   -> ('Maths', 'Science')       -> TUPLE
# kwargs -> {'name': 'Prabhat', ...}   -> DICTIONARY


# ============================================================
# 5. PACKING
# ============================================================

# Packing = collecting multiple arguments into one object.

def student(*args, **kwargs):
    pass

student("Maths", "Science", name="Prabhat", age=20)

# Positional arguments
#       ↓
#     *args
#       ↓
# ('Maths', 'Science')
#
# Keyword arguments
#       ↓
#    **kwargs
#       ↓
# {'name': 'Prabhat', 'age': 20}


# ============================================================
# 6. UNPACKING
# ============================================================

# Unpacking = taking values from a collection and passing
# them as separate arguments.


# LIST:

courses = ["Maths", "Science", "English"]

def student(a, b, c):
    print(a, b, c)

student(*courses)

# *courses:
#
# ["Maths", "Science", "English"]
#              ↓
#             *
#              ↓
# "Maths", "Science", "English"


# TUPLE:

courses = ("Maths", "Science", "English")

student(*courses)

# * works with BOTH lists and tuples.


# DICTIONARY:

info = {
    "name": "Prabhat",
    "age": 20
}

def student(name, age):
    print(name, age)

student(**info)

# **info:
#
# {"name": "Prabhat", "age": 20}
#              ↓
#             **
#              ↓
# name="Prabhat", age=20


# ============================================================
# 7. WHEN IS * NEEDED?
# ============================================================

# Values written individually:
#
student("Maths", "Science", "English")
#
# No * needed because they are already separate arguments.


# Values inside a list/tuple:
#
courses = ["Maths", "Science", "English"]
student(*courses)
#
# * is needed to UNPACK the collection.


# A tuple passed directly as ONE argument:
#
student(("Maths", "Science", "English"))
#
# This passes ONE argument: the entire tuple.


# Tuple unpacked into separate arguments:
#
student(*("Maths", "Science", "English"))
#
# * is needed.


# IMPORTANT:
#
# * is NOT only for variables.
# * means:
# "Unpack this iterable into positional arguments."
#
# It can work with lists, tuples, strings, etc.


# ============================================================
# 8. PACKING vs UNPACKING
# ============================================================

# PACKING:
#
# Many arguments
#      ↓
#    *args
#      ↓
# One tuple
#
#
# UNPACKING:
#
# One list/tuple
#      ↓
#      *
#      ↓
# Many arguments


# SIMPLE RULE:
#
# *args       -> PACK positional arguments into a tuple
# *list       -> UNPACK list into positional arguments
# *tuple      -> UNPACK tuple into positional arguments
#
# **kwargs    -> PACK keyword arguments into a dictionary
# **dict      -> UNPACK dictionary into keyword arguments


# ============================================================
# 9. COMPLETE EXAMPLE
# ============================================================

def student(*args, **kwargs):
    print("Courses:", args)
    print("Info:", kwargs)


courses = ["Maths", "Science", "English", "Hindi"]

info = {
    "name": "Prabhat",
    "age": 20
}

student(*courses, **info)

# *courses -> UNPACKS the list
# **info   -> UNPACKS the dictionary
#
# The function receives:
#
# "Maths", "Science", "English", "Hindi",
# name="Prabhat", age=20
#
# Then:
#
# *args    -> PACKS positional arguments into a tuple
# **kwargs -> PACKS keyword arguments into a dictionary


# ============================================================
# 10. QUICK TABLE
# ============================================================

# | Syntax      | Purpose                       | Result       |
# |-------------|-------------------------------|--------------|
# | *args       | Collect positional arguments  | tuple        |
# | **kwargs    | Collect keyword arguments     | dictionary   |
# | *list       | Unpack list                   | arguments    |
# | *tuple      | Unpack tuple                  | arguments    |
# | **dict      | Unpack dictionary             | arguments    |


# ============================================================
# 11. TYPE HINTS
# ============================================================

# Type hints tell us what type of value is expected.
# Python does NOT automatically enforce them.

def add(a: int, b: int) -> int:
    return a + b

name: str = "Prabhat"
age: int = 20
price: float = 99.5
is_student: bool = True


# List:

numbers: list[int] = [1, 2, 3]

names: list[str] = ["Prabhat", "MJ"]


# Dictionary:

student_info: dict[str, int] = {
    "age": 20
}


# Function:

def greet(name: str) -> str:
    return f"Hello {name}"


# IMPORTANT:
#
# def function(parameter: expected_type) -> return_type:
#
# Example:
#
# def square(number: int) -> int:
#     return number * number
#
# number: int
#     -> parameter should be an int
#
# -> int
#     -> function is expected to return an int


# ============================================================
# 12. WHY TYPE HINTS?
# ============================================================

# Type hints make code:
#
# - easier to understand
# - easier to maintain
# - easier for IDEs to check
# - easier to debug
# - better for larger projects
#
# They are especially useful in AI/ML projects.


# ============================================================
# 13. MODULES
# ============================================================

# Module = a single Python file (.py)
#
# Example:
#
# calculator.py
#
# A module can contain:
# - functions
# - classes
# - variables


# Import from a module:

from calculator import add

print(add(10, 20))


# ============================================================
# 14. PACKAGES
# ============================================================

# Package = a folder containing related Python modules.
#
# Example:
#
# myproject/
#     main.py
#     utils/
#         __init__.py
#         calculator.py
#         file.py
#
#
# Here:
#
# calculator.py -> MODULE
# file.py       -> MODULE
# utils/        -> PACKAGE


# ============================================================
# 15. IMPORTING FROM A PACKAGE
# ============================================================

# Example:
#
# myproject/
#     main.py
#     utils/
#         __init__.py
#         calculator.py
#
#
# In main.py:
#
# from utils.calculator import add
#
# print(add(10, 20))


# ============================================================
# 16. MODULE vs PACKAGE
# ============================================================

# MODULE
#     = one Python file (.py)
#
# PACKAGE
#     = folder containing related Python modules
#
#
# Easy memory:
#
# module  = one file
# package = collection of modules


# ============================================================
# FINAL MEMORY SHEET
# ============================================================

# PARAMETER
#     Variable in function definition.
#
# ARGUMENT
#     Actual value passed to a function.
#
# *args
#     Multiple positional arguments → tuple.
#
# **kwargs
#     Multiple keyword arguments → dictionary.
#
# *list / *tuple
#     Unpack into positional arguments.
#
# **dict
#     Unpack into keyword arguments.
#
# PACKING
#     Many arguments → one tuple/dictionary.
#
# UNPACKING
#     One collection → many arguments.
#
# TYPE HINT
#     Indicates the expected type of a value.
#
# MODULE
#     One .py file.
#
# PACKAGE
#     Collection of related Python modules.
#
#
# ============================================================
# MOST IMPORTANT:
#
# *args       → positional arguments → tuple
# **kwargs    → keyword arguments  → dictionary
#
# *list       → unpack
# *tuple      → unpack
# **dict      → unpack
#
# *args / **kwargs → used when DEFINING a function
# * / **          → used for UNPACKING when CALLING a function
# ============================================================