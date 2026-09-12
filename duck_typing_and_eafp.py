class Person:
    def feature(self):
        print("I am a person with unique features.")


class dog:
    def feature(self):
        print("I am a dog with unique features.")
        
class call_function:
    def call(self,obj):
        obj.feature()


p = Person()
d = dog()

p.feature()  # Output: I am a person with unique features.
d.feature()  # Output: I am a dog with unique features.

c = call_function()

c.call(p)  # Output: I am a person with unique features.
c.call(d)  # Output: I am a dog with unique features.


# Duck Typing and EAFP in Python

## 1. Duck Typing

### Definition

# Duck Typing means:

# > "If an object behaves like the required type, we can use it as that type."

# Python does not always care about the object's actual type. It cares about **what the object can do**.

# ### Example

# ```python
# class Dog:
#     def speak(self):
#         print("Woof!")


# class Cat:
#     def speak(self):
#         print("Meow!")


# def make_sound(animal):
#     animal.speak()


# make_sound(Dog())
# make_sound(Cat())
# ```

# ### Output

# ```text
# Woof!
# Meow!
# ```

# Here, `make_sound()` does not check whether the object is a `Dog` or `Cat`.

# It only expects the object to have a `speak()` method.

# ### Important Point

# ```text
# Behavior matters more than type.
# ```

# Instead of asking:

# ```python
# if isinstance(animal, Dog):
# ```

# Python can simply try:

# ```python
# animal.speak()
# ```

# If the object has `speak()`, it works.

# ---

# # 2. EAFP

# ### Full Form

# ```text
# EAFP = Easier to Ask for Forgiveness than Permission
# ```

# ### Definition

# EAFP is a Python programming style where we:

# 1. Try to perform an operation.
# 2. If it fails, handle the exception.

# Instead of checking whether something will work **before** doing it, we simply try it.

# ### Example

# ```python
# data = {"name": "Prabhat"}

# try:
#     print(data["age"])
# except KeyError:
#     print("Age does not exist")
# ```

# ### Output

# ```text
# Age does not exist
# ```

# Here, we don't first check:

# ```python
# if "age" in data:
# ```

# Instead, we try to access `"age"` and handle the `KeyError`.

# ---

# # 3. EAFP vs LBYL

# Another common programming style is:

# ```text
# LBYL = Look Before You Leap
# ```

# It checks whether an operation is possible before performing it.

# ### LBYL Example

# ```python
# data = {"name": "Prabhat"}

# if "age" in data:
#     print(data["age"])
# else:
#     print("Age does not exist")
# ```

# ### EAFP Example

# ```python
# data = {"name": "Prabhat"}

# try:
#     print(data["age"])
# except KeyError:
#     print("Age does not exist")
# ```

# ### Difference

# ```text
# LBYL:
# Check first → Perform operation

# EAFP:
# Perform operation → Handle failure
# ```

# ---

# # 4. Duck Typing + EAFP

# Duck typing and EAFP are commonly used together.

# ### Example

# ```python
# def get_length(obj):
#     try:
#         return len(obj)
#     except TypeError:
#         return "Object has no length"


# print(get_length([1, 2, 3]))
# print(get_length("Python"))
# print(get_length(10))
# ```

# ### Output

# ```text
# 3
# 6
# Object has no length
# ```

# The function does not check whether `obj` is a list, string, tuple, etc.

# It simply tries:

# ```python
# len(obj)
# ```

# If it works → use the result.

# If it fails → handle the exception.

# ---

# # 5. Why Python Uses EAFP

# EAFP is useful because:

# * Code is often shorter.
# * It focuses on the operation instead of checking types.
# * It works well with duck typing.
# * It handles unexpected situations using exceptions.
# * It avoids unnecessary type checking.

# ---

# # 6. Important Example

# ### Without Duck Typing

# ```python
# def print_data(obj):
#     if isinstance(obj, list):
#         print(obj)
#     elif isinstance(obj, tuple):
#         print(obj)
# ```

# This restricts the function to specific types.

# ### With Duck Typing

# ```python
# def print_data(obj):
#     print(obj)
# ```

# The function doesn't care about the exact type.

# It only cares that the object can be printed.

# ---

# # 7. Real-World Example

# Suppose a function needs an object with a `save()` method.

# ```python
# def save_data(obj):
#     try:
#         obj.save()
#     except AttributeError:
#         print("Object cannot be saved")
# ```

# Any object with a `save()` method can be passed:

# ```python
# class File:
#     def save(self):
#         print("File saved")


# class Database:
#     def save(self):
#         print("Data saved")


# save_data(File())
# save_data(Database())
# ```

# The function doesn't care whether the object is a `File` or `Database`.

# It only cares that it supports:

# ```python
# save()
# ```

# This is **Duck Typing + EAFP**.

# ---

# # 8. Key Points to Remember

# ```text
# Duck Typing:
# Focus on what an object can DO, not what type it IS.

# EAFP:
# Try the operation first and handle the exception if it fails.

# LBYL:
# Check whether the operation is possible before performing it.
# ```

# ### Easy Memory Trick

# ```text
# Duck Typing → "Can you do it?"

# EAFP → "Try it. If it fails, handle it."

# LBYL → "Check first, then do it."
# ```

# ### Python Philosophy

# Python generally prefers:

# ```python
# try:
#     operation()
# except SomeError:
#     handle_error()
# ```

# over excessive type checking when the operation itself can safely determine whether it works.


