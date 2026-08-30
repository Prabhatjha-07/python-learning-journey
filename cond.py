# lang = 'french'


# if lang == 'english':
#     print("condition was true")

# elif lang == 'french':
#     print("condition is true")
# else:
#     print('false')

# user = 'admin'
# login = True

# if user == 'admin' and login :
#     print('welcome admin')
# else:
#     print('you are not admin')
    
# if user == 'admin' or login :
#     print('welcome admin')
# else:
#     print('you are not admin')
    
# if not login:
#     print('you are not logged in ')
# else:
#     print('you are logged in')

# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 5]

# print(a == b)
# print(id(a))
# print(id(b))
# print(a is b)





# Python Conditionals — My Notes

| Topic           | Syntax / Example            | Description                                  |
| --------------- | --------------------------- | -------------------------------------------- |
| `if`            | `if condition:`             | Runs code when condition is `True`           |
| `else`          | `else:`                     | Runs when `if` condition is `False`          |
| `elif`          | `elif condition:`           | Checks another condition                     |
| Boolean         | `login = True`              | `True` or `False` value                      |
| Comparison `==` | `lang == 'english'`         | Checks if two values are equal               |
| Logical `and`   | `user == 'admin' and login` | Both conditions must be `True`               |
| Logical `or`    | `user == 'admin' or login`  | At least one condition must be `True`        |
| Logical `not`   | `not login`                 | Reverses `True`/`False`                      |
| `==` vs `=`     | `x == 5` / `x = 5`          | `==` compares; `=` assigns                   |
| `is`            | `a is b`                    | Checks if two variables are the same object  |
| `==` vs `is`    | `a == b` / `a is b`         | `==` checks values; `is` checks identity     |
| `id()`          | `id(a)`                     | Returns an object's identity                 |
| Lists           | `a = [1,2,3]`               | Collection of values                         |
| List comparison | `a == b`                    | Checks whether list contents are equal       |
| List identity   | `a is b`                    | Checks whether both refer to the same object |

---

## `if`, `elif`, `else`

| Keyword | Purpose                 | Example                  |
| ------- | ----------------------- | ------------------------ |
| `if`    | First condition         | `if lang == 'english':`  |
| `elif`  | Another condition       | `elif lang == 'french':` |
| `else`  | If no condition is true | `else:`                  |

```python id="b9w3q7"
lang = 'french'

if lang == 'english':
    print("condition was true")

elif lang == 'french':
    print("condition is true")

else:
    print("false")
```

| Situation           | Result          |
| ------------------- | --------------- |
| `lang == 'english'` | First `if` runs |
| `lang == 'french'`  | `elif` runs     |
| Anything else       | `else` runs     |

---

## `and`

| Item  | Meaning                      |
| ----- | ---------------------------- |
| `and` | Both conditions must be true |

```python id="f8z2q1"
user = 'admin'
login = True

if user == 'admin' and login:
    print('welcome admin')
else:
    print('you are not admin')
```

| User is admin | Logged in | Result  |
| ------------- | --------- | ------- |
| True          | True      | `True`  |
| True          | False     | `False` |
| False         | True      | `False` |
| False         | False     | `False` |

---

## `or`

| Item | Meaning                             |
| ---- | ----------------------------------- |
| `or` | At least one condition must be true |

```python id="d1x8q4"
if user == 'admin' or login:
    print('welcome admin')
else:
    print('you are not admin')
```

| Condition 1 | Condition 2 | Result  |
| ----------- | ----------- | ------- |
| True        | True        | `True`  |
| True        | False       | `True`  |
| False       | True        | `True`  |
| False       | False       | `False` |

---

## `not`

| Item  | Meaning                  |
| ----- | ------------------------ |
| `not` | Reverses a Boolean value |

```python id="p6m3x9"
login = False

if not login:
    print('you are not logged in')
else:
    print('you are logged in')
```

| `login` | `not login` |
| ------- | ----------- |
| `True`  | `False`     |
| `False` | `True`      |

---

## `==` vs `is`

| Operator | Checks          | Example  |
| -------- | --------------- | -------- |
| `==`     | Value/content   | `a == b` |
| `is`     | Object identity | `a is b` |

Example:

```python id="r4k7w2"
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

print(a == b)
print(a is b)
```

| Expression | Result  | Why                                 |
| ---------- | ------- | ----------------------------------- |
| `a == b`   | `True`  | Both lists contain the same values  |
| `a is b`   | `False` | They are two different list objects |

---

## `id()`

| Function | Purpose                           | Example |
| -------- | --------------------------------- | ------- |
| `id()`   | Returns the identity of an object | `id(a)` |

```python id="n2c5v8"
print(id(a))
print(id(b))
```

If `a` and `b` are separate objects, their IDs will normally be different.

---

## Lists + `==` + `is`

| Code            | Meaning              |
| --------------- | -------------------- |
| `a = [1, 2, 3]` | Creates a list       |
| `b = [1, 2, 3]` | Creates another list |
| `a == b`        | Same contents?       |
| `a is b`        | Same object?         |
| `id(a)`         | Identity of `a`      |
| `id(b)`         | Identity of `b`      |

### Main idea

| Question                         | Use    |
| -------------------------------- | ------ |
| "Do they have the same value?"   | `==`   |
| "Are they the same object?"      | `is`   |
| "What is the object's identity?" | `id()` |

---

## Your Current Conditional Cheat Sheet

| Operator / Keyword | Meaning                    |
| ------------------ | -------------------------- |
| `if`               | Check a condition          |
| `elif`             | Check another condition    |
| `else`             | Run if all conditions fail |
| `==`               | Equal value                |
| `and`              | Both true                  |
| `or`               | At least one true          |
| `not`              | Reverse true/false         |
| `is`               | Same object                |
| `id()`             | Object identity            |

---

## Rules You Have Learned

| Rule                                   | Example              |
| -------------------------------------- | -------------------- |
| Conditions use `:`                     | `if login:`          |
| Code inside condition must be indented | `    print("Hello")` |
| `=` assigns a value                    | `login = True`       |
| `==` compares values                   | `login == True`      |
| `and` requires both conditions         | `admin and login`    |
| `or` requires at least one             | `admin or login`     |
| `not` reverses the condition           | `not login`          |
| `==` compares values                   | `a == b`             |
| `is` compares identity                 | `a is b`             |
| `id()` shows object identity           | `id(a)`              |

---

## Everything Covered So Far

|  # | Concept                  | Covered |
| -: | ------------------------ | :-----: |
|  1 | `if`                     |    ✅    |
|  2 | `elif`                   |    ✅    |
|  3 | `else`                   |    ✅    |
|  4 | Boolean `True` / `False` |    ✅    |
|  5 | `==`                     |    ✅    |
|  6 | `and`                    |    ✅    |
|  7 | `or`                     |    ✅    |
|  8 | `not`                    |    ✅    |
|  9 | `=` vs `==`              |    ✅    |
| 10 | Lists                    |    ✅    |
| 11 | `==` with lists          |    ✅    |
| 12 | `is`                     |    ✅    |
| 13 | `==` vs `is`             |    ✅    |
| 14 | `id()`                   |    ✅    |
| 15 | List identity            |    ✅    |
