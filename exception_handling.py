# # Python: Try/Except Error Handling

# ## 1. What is Exception Handling?

# Exception handling is used to handle **runtime errors** without stopping the entire program.

# Python uses:

# * `try`
# * `except`
# * `else`
# * `finally`

# ---

# ## 2. Basic Syntax

# ```python
# try:
#     # Code that may cause an error
# except:
#     # Code executed if an error occurs
# ```

# Example:

# ```python
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except:
#     print("Something went wrong!")
# ```

# ---

# ## 3. Handling Specific Exceptions

# It is better to catch a **specific exception** instead of using a general `except`.

# ```python
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# ```

# Common exceptions:

# ```text
# ValueError          → Invalid value
# TypeError           → Wrong data type
# ZeroDivisionError   → Division by zero
# IndexError          → Invalid list index
# KeyError            → Missing dictionary key
# FileNotFoundError   → File does not exist
# NameError           → Variable is not defined
# ```

# ---

# ## 4. Multiple Exceptions

# Multiple exceptions can be handled together:

# ```python
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except (ValueError, ZeroDivisionError):
#     print("Invalid input or division by zero.")
# ```

# ---

# ## 5. Using `else`

# The `else` block executes **only when no exception occurs**.

# ```python
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input.")
# else:
#     print("You entered:", num)
# ```

# Flow:

# ```text
# try
#  ↓
# Error?
#  ├── Yes → except
#  └── No  → else
# ```

# ---

# ## 6. Using `finally`

# The `finally` block **always executes**, whether an exception occurs or not.

# ```python
# try:
#     file = open("data.txt", "r")
#     print(file.read())
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Program finished.")
# ```

# `finally` is commonly used for **cleanup operations**, such as closing files or releasing resources.

# ---

# ## 7. Getting the Error Message

# Use `as` to store the exception object:

# ```python
# try:
#     num = int("abc")
# except ValueError as e:
#     print("Error:", e)
# ```

# Output:

# ```text
# Error: invalid literal for int() with base 10: 'abc'
# ```

# ---

# ## 8. Raising an Exception

# Use `raise` when you want to manually generate an exception.

# ```python
# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative.")
# ```

# ---

# ## 9. Complete Example

# ```python
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     result = num1 / num2

# except ValueError:
#     print("Please enter numbers only.")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# else:
#     print("Result:", result)

# finally:
#     print("Execution completed.")
# ```

# ## 10. Important Points

# * `try` → contains risky code.
# * `except` → handles the error.
# * `else` → runs when there is no error.
# * `finally` → always runs.
# * `raise` → manually raises an exception.
# * Prefer **specific exceptions** over a general `except`.
# * Exception handling prevents unexpected errors from crashing the program.

# ### Basic Structure

# ```python
# try:
#     # Risky code
# except ExceptionType:
#     # Handle error
# else:
#     # Runs if no error
# finally:
#     # Always runs
# ```
