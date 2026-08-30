student = {
    "name": "prabhat",
    "age": 20,
    "subjects": ['math','science','english']
    }
# student['phone'] = '222-222'
# print(student)
# student.update({'name': 'jane' , 'age': '23'})
# print(student)
# print(student["name"] ,student["age"])
# print(student.get('name'))
# print(student.get('phone' , ' not found '))
# del student['age']
# student.pop('name')
# print(student)


# print(student.keys())
# print(student.values())
# print(student.items())
for key in student:
    print(key)

for key , value in student.items():
    print(key , value)\
        
        

| **Topic**                            | **Syntax**                             | **Description**                                                                 | **Example**                                            |                 |        |
| ------------------------------------ | -------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------- | ------ |
| **Create Dictionary**                | `dict_name = {key: value}`             | Creates a dictionary with key-value pairs.                                      | `student = {"name": "Prabhat", "age": 20}`             |                 |        |
| **Access Value (`[]`)**              | `dict[key]`                            | Returns the value of the given key. Raises `KeyError` if the key doesn't exist. | `student["name"]`                                      |                 |        |
| **Access Value (`get()`)**           | `dict.get(key)`                        | Returns the value if the key exists, otherwise returns `None`.                  | `student.get("name")`                                  |                 |        |
| **`get()` with Default**             | `dict.get(key, default)`               | Returns the default value if the key doesn't exist.                             | `student.get("phone", "Not Found")`                    |                 |        |
| **Add New Item**                     | `dict[key] = value`                    | Adds a new key-value pair or updates an existing key.                           | `student["phone"] = "222-222"`                         |                 |        |
| **Update Items**                     | `dict.update({...})`                   | Updates one or more key-value pairs.                                            | `student.update({"age": 21})`                          |                 |        |
| **Delete Item**                      | `del dict[key]`                        | Deletes the specified key-value pair.                                           | `del student["age"]`                                   |                 |        |
| **Remove Item**                      | `dict.pop(key)`                        | Removes the key and returns its value.                                          | `student.pop("phone")`                                 |                 |        |
| **Remove Last Item**                 | `dict.popitem()`                       | Removes and returns the last inserted key-value pair.                           | `student.popitem()`                                    |                 |        |
| **Clear Dictionary**                 | `dict.clear()`                         | Removes all items from the dictionary.                                          | `student.clear()`                                      |                 |        |
| **Copy Dictionary**                  | `dict.copy()`                          | Returns a shallow copy of the dictionary.                                       | `copy_student = student.copy()`                        |                 |        |
| **Length**                           | `len(dict)`                            | Returns the number of key-value pairs.                                          | `len(student)`                                         |                 |        |
| **Check Key Exists**                 | `key in dict`                          | Returns `True` if the key exists.                                               | `"name" in student`                                    |                 |        |
| **Get All Keys**                     | `dict.keys()`                          | Returns a view of all keys.                                                     | `student.keys()`                                       |                 |        |
| **Get All Values**                   | `dict.values()`                        | Returns a view of all values.                                                   | `student.values()`                                     |                 |        |
| **Get All Items**                    | `dict.items()`                         | Returns key-value pairs as tuples.                                              | `student.items()`                                      |                 |        |
| **Loop Through Keys**                | `for key in dict:`                     | Iterates through all keys.                                                      | `for key in student: print(key)`                       |                 |        |
| **Loop Through Keys (`keys()`)**     | `for key in dict.keys():`              | Another way to iterate through keys.                                            | `for key in student.keys(): print(key)`                |                 |        |
| **Loop Through Values**              | `for value in dict.values():`          | Iterates through all values.                                                    | `for value in student.values(): print(value)`          |                 |        |
| **Loop Through Key-Value Pairs**     | `for key, value in dict.items():`      | Iterates through keys and values together.                                      | `for key, value in student.items(): print(key, value)` |                 |        |
| **Nested Dictionary**                | `dict = {"key": {"inner": value}}`     | A dictionary inside another dictionary.                                         | `students["student1"]["name"]`                         |                 |        |
| **Dictionary Comprehension**         | `{key: value for item in iterable}`    | Creates a dictionary using a loop.                                              | `{x: x*x for x in range(5)}`                           |                 |        |
| **Create with `dict()`**             | `dict(key=value)`                      | Creates a dictionary using keyword arguments.                                   | `person = dict(name="Prabhat", age=20)`                |                 |        |
| **Create from Keys**                 | `dict.fromkeys(keys, value)`           | Creates a dictionary using a list of keys.                                      | `dict.fromkeys(["a","b"], 0)`                          |                 |        |
| **Merge Dictionaries (Python 3.9+)** | `dict1                                 | dict2`                                                                          | Combines two dictionaries into a new one.              | `merged = dict1 | dict2` |
| **Merge with `update()`**            | `dict1.update(dict2)`                  | Adds items from one dictionary into another.                                    | `dict1.update(dict2)`                                  |                 |        |
| **Set Default Value**                | `dict.setdefault(key, value)`          | Returns the value if key exists; otherwise adds the key with the default value. | `student.setdefault("age", 20)`                        |                 |        |
| **Duplicate Keys**                   | `{"a":1, "a":2}`                       | Duplicate keys are **not allowed**. The last value overwrites the previous one. | `{"a":2}`                                              |                 |        |
| **Duplicate Values**                 | `{"a":1, "b":1}`                       | Duplicate values **are allowed**.                                               | `{"a":1, "b":1}`                                       |                 |        |
| **Mutable**                          | —                                      | Dictionaries can be modified after creation.                                    | Add, update, or delete items.                          |                 |        |
| **Ordered**                          | —                                      | Dictionaries preserve insertion order (Python 3.7+).                            | Items appear in the order they were added.             |                 |        |
| **Unique Keys**                      | —                                      | Every key must be unique.                                                       | `"name"` can appear only once.                         |                 |        |
| **Allowed Key Types**                | `str`, `int`, `float`, `bool`, `tuple` | Keys must be immutable (hashable).                                              | `"name"`, `1`, `(1,2)`                                 |                 |        |
| **Not Allowed Key Types**            | `list`, `dict`, `set`                  | Mutable objects cannot be used as keys.                                         | ❌ `{[1,2]: "value"}`                                   |                 |        |
| **Time Complexity (Access)**         | `dict[key]`                            | Average case **O(1)**.                                                          | Fast lookup.                                           |                 |        |
| **Time Complexity (Insert)**         | `dict[key] = value`                    | Average case **O(1)**.                                                          | Fast insertion.                                        |                 |        |
| **Time Complexity (Delete)**         | `del dict[key]`                        | Average case **O(1)**.                                                          | Fast deletion.                                         |                 |        |
| **Time Complexity (Search Key)**     | `key in dict`                          | Average case **O(1)**.                                                          | `"age" in student`                                     |                 |        |
| **Time Complexity (Loop)**           | `for key in dict:`                     | **O(n)** because every item is visited.                                         | Loop through all items.                                |                 |        |
