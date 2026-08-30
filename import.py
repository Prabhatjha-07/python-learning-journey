# import module as mm
# import sys

# from module import search
import calendar
import datetime
import math
import os
import random

courses = ['math' , 'science' , 'nepali' , 'comp' , ' social']

# print(mm.search(courses , 'nepali'))
# print(search(courses , 'nepali'))
# print(sys.path)

print(random.choice(courses))
print(math.radians(90))

print(datetime.date.today())  # noqa: DTZ011
print(calendar.isleap(2020))
print(os.getcwd())


# ============================================================
# PYTHON: MODULES, IMPORTS & STANDARD LIBRARY
# ============================================================


# ============================================================
# 1. MODULE
# ============================================================

# A module is a Python file (.py) containing reusable code.
#
# Example:
#
# module.py
#
# def find_index(items, target):
#     for i, value in enumerate(items):
#         if value == target:
#             return i
#     return -1
#
# main.py
#
# import module
# print(module.find_index(["math", "nepali"], "nepali"))


# ============================================================
# 2. import
# ============================================================

# Imports the whole module.

import math

# Use:
# math.sqrt(25)
# math.pi


# ============================================================
# 3. import AS
# ============================================================

# Gives a module a shorter alias.

import math as m

# Use:
# m.sqrt(25)
#
# Common AI/ML examples:
#
# import numpy as np
# import pandas as pd


# ============================================================
# 4. from ... import
# ============================================================

# Imports a specific function/object from a module.

from math import sqrt

# Use directly:
# sqrt(25)


# Multiple imports:

from math import sqrt, ceil, floor


# With an alias:

from math import sqrt as square_root

# square_root(25)


# Avoid:
#
# from math import *
#
# It imports everything and can cause naming conflicts.


# ============================================================
# 5. STANDARD LIBRARY
# ============================================================

# Python provides many modules without requiring installation.
# These are called the Standard Library.

# Important modules for you:
#
# math       -> mathematical functions
# random     -> random values
# datetime   -> dates and times
# calendar   -> calendar operations
# os         -> operating-system/file operations
# sys        -> Python interpreter information
# json       -> JSON data
# pathlib    -> file/directory paths
# collections -> specialized containers
# statistics -> statistical calculations


# ============================================================
# 6. math
# ============================================================

import math

# Square root:
# math.sqrt(25)          -> 5.0

# Power:
# math.pow(2, 3)         -> 8.0

# Round upward:
# math.ceil(4.2)         -> 5

# Round downward:
# math.floor(4.8)        -> 4

# Factorial:
# math.factorial(5)      -> 120

# Constants:
# math.pi
# math.e

# Degrees -> radians:
# math.radians(90)

# Radians -> degrees:
# math.degrees(math.pi)


# ============================================================
# 7. random
# ============================================================

import random

courses = ["math", "science", "nepali", "computer"]

# Random item:
# random.choice(courses)

# Random integer INCLUDING both limits:
# random.randint(1, 10)

# Random float:
# random.random()
# Range: 0.0 <= value < 1.0

# Random unique items:
# random.sample(courses, 2)

# Shuffle a list:
# random.shuffle(courses)
# Changes the original list.


# ============================================================
# 8. datetime
# ============================================================

import datetime

# Today's date:
today = datetime.date.today()

# today.year
# today.month
# today.day

# Current date and time:
now = datetime.datetime.now()

# now.year
# now.month
# now.day
# now.hour
# now.minute
# now.second

# Create a date:
# date = datetime.date(2026, 8, 12)

# Difference between dates:
#
# date1 = datetime.date(2026, 8, 12)
# date2 = datetime.date(2026, 12, 12)
# difference = date2 - date1
# print(difference.days)


# ============================================================
# 9. calendar
# ============================================================

import calendar

# Check leap year:
# calendar.isleap(2024)      -> True
# calendar.isleap(2023)      -> False

# Display a month's calendar:
# print(calendar.month(2026, 8))

# Get weekday:
# calendar.weekday(2026, 8, 12)
#
# 0 = Monday
# 1 = Tuesday
# 2 = Wednesday
# 3 = Thursday
# 4 = Friday
# 5 = Saturday
# 6 = Sunday


# ============================================================
# 10. os
# ============================================================

import os

# Current working directory:
# os.getcwd()

# List files/folders:
# os.listdir()

# Change working directory:
# os.chdir("path")

# Check whether a path exists:
# os.path.exists("students.json")

# Check if it is a file:
# os.path.isfile("students.json")

# Check if it is a directory:
# os.path.isdir("project")

# Join paths:
# os.path.join("data", "students.json")


# ============================================================
# 11. pathlib
# ============================================================

# pathlib is a modern way to work with file paths.

from pathlib import Path

# Create a path:
# path = Path("data") / "students.json"

# Check existence:
# path.exists()

# Check file:
# path.is_file()

# Check directory:
# path.is_dir()


# ============================================================
# 12. sys
# ============================================================

import sys

# Python version:
# print(sys.version)

# Python executable:
# print(sys.executable)

# Locations Python searches for imports:
# print(sys.path)


# ============================================================
# 13. json
# ============================================================

import json

# Python dictionary:
#
# student = {
#     "Name": "Prabhat",
#     "Grade": 12
# }

# Write Python data -> JSON:
#
# with open("student.json", "w") as file:
#     json.dump(student, file, indent=4)

# Read JSON -> Python object:
#
# with open("student.json", "r") as file:
#     student = json.load(file)


# ============================================================
# 14. MODULE ALIAS
# ============================================================

# Suppose module.py contains:
#
# def find_index(items, target):
#     for i, value in enumerate(items):
#         if value == target:
#             return i
#     return -1

# Import with alias:
#
# import module as mm
#
# courses = ["math", "science", "nepali"]
#
# print(mm.find_index(courses, "nepali"))
#
# Output:
# 2


# ============================================================
# 15. FUNCTION FROM A MODULE
# ============================================================

# Instead of:
#
# import module
# module.find_index(...)

# You can write:
#
# from module import find_index
#
# find_index(courses, "nepali")


# ============================================================
# 16. MODULE SEARCH PATH
# ============================================================

# When Python sees:
#
# import module
#
# Python searches locations stored in:
#
# sys.path
#
# You can see them using:
#
# import sys
# print(sys.path)
#
# This helps when debugging:
#
# ModuleNotFoundError
#
# or importing the wrong module.


# ============================================================
# 17. __name__ == "__main__"
# ============================================================

# Common Python pattern:

def main():
    print("Program started")


if __name__ == "__main__":
    main()


# If the file is executed directly:
#
# python file.py
#
# __name__ == "__main__"
#
# If the file is imported:
#
# import file
#
# __name__ is the module's name instead.


# ============================================================
# 18. MODULE vs PACKAGE
# ============================================================

# MODULE:
# A single .py file.
#
# Example:
# math_utils.py
#
#
# PACKAGE:
# A directory containing Python modules.
#
# Example:
#
# project/
#     main.py
#     utilities/
#         math_utils.py
#         file_utils.py


# ============================================================
# 19. THIRD-PARTY LIBRARIES
# ============================================================

# Third-party libraries are not part of Python's standard
# library and usually need to be installed.

# Example:
#
# pip install numpy
# pip install pandas
#
# Then:
#
# import numpy as np
# import pandas as pd


# ============================================================
# 20. STANDARD LIBRARY vs THIRD-PARTY
# ============================================================

# Standard Library:
#
# import math
# import random
# import os
# import json
#
# Usually no installation required.


# Third-party:
#
# import numpy
# import pandas
# import sklearn
# import torch
#
# Usually installed using pip.


# ============================================================
# 21. IMPORTANT AI/ML IMPORTS TO KNOW LATER
# ============================================================

# NumPy:
# import numpy as np

# Pandas:
# import pandas as pd

# Matplotlib:
# import matplotlib.pyplot as plt

# Scikit-learn:
# import sklearn

# PyTorch:
# import torch


# ============================================================
# 22. IMPORTANT RULES
# ============================================================

# Python is case-sensitive.

# find_index != find_Index

# calendar != calender


# If you write:
#
# import module as mm
#
# then use:
#
# mm.function()


# If you write:
#
# from module import function
#
# then use:
#
# function()


# ============================================================
# 23. WHAT TO LEARN NEXT
# ============================================================

# Recommended order:
#
# 1. Modules and imports             <- CURRENT
# 2. __name__ == "__main__"
# 3. Packages
# 4. pip
# 5. Virtual environments
# 6. NumPy
# 7. Pandas
# 8. Matplotlib
# 9. Statistics & Probability
# 10. Machine Learning
# 11. PyTorch
#
#
# Do NOT try to memorize every function.
#
# Learn:
# - What a module does
# - How to import it
# - How to access its functions
# - How to find documentation when needed