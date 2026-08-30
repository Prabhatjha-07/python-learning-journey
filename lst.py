

# courses = ['history', 'math', 'physics', 'compsci']
# print(len(courses))
# print(courses[2])
# print(courses[-1])
# print(courses[0:3])
# print(courses[:3])
# print(courses[1:])
# courses.append('mj')
# courses.insert(1, 'art')

# print(courses)
# print(courses.index('math'))
# print('math' in courses)

# courses1 = ['art', 'education']
# courses.extend(courses1)
# print(courses)
# courses.insert(0, courses1)
# print(courses)
# courses.remove('art')
# print(courses)
# courses.pop()
# print(courses)
# courses.remove('art')
# print(courses)
# courses.reverse()
# print(courses)
# courses.sort()
# print(courses)
# nums = [1, 5, 2, 4, 3]
# nums.sort()
# print(nums)
# nums.sort(reverse=True )
# print(nums)
# print(min(nums) )
# print(max(nums) )
# print(sum(nums) )

# sorted_courses = sorted(courses)
# print(sorted_courses)

# for mj in courses:
#     print(mj)
    
# for index , course in enumerate(courses , start = 1):
#     print(index, course)
    
# cou_str = ' , '.join(courses)
# print(cou_str)

# mou_str = ' - '.join(courses)
# print(mou_str)

# new_list = cou_str.split(' , ')
# print(new_list)


# tuple = ('history', 'math', 'physics', 'compsci')


# set = {'history', 'math', 'physics', 'compsci', 'math'}
# print(set)
# cs_set = {'history', 'math', 'art', 'design'}
# print(set.intersection(cs_set)) #prints the common values in both sets
# print(set.difference(cs_set)) #prints the values that are in set but not in cs
# print(set.union(cs_set)) #prints all the values in both sets

# #sets deals with the unique values and it does not maintain the order of the elements also removing any duplicates from the list

# empty_set = {}
# empty_set = set()

# empty_list = []
# empty_list = list()


# empty_tuple = ()
# empty_tuple = tuple()


1. List


| Topic           | Syntax                    | Description                               | Working                       | Example                                    |
| --------------- | ------------------------- | ----------------------------------------- | ----------------------------- | ------------------------------------------ |
| Create List     | `list_name = [ ]`         | Creates an ordered, mutable collection.   | Stores multiple values.       | `courses = ['history', 'math', 'physics']` |
| Length          | `len(list)`               | Returns the number of elements.           | Counts all items.             | `len(courses)` → `3`                       |
| Indexing        | `list[index]`             | Accesses an element using its index.      | Index starts at **0**.        | `courses[1]` → `'math'`                    |
| Negative Index  | `list[-1]`                | Accesses elements from the end.           | `-1` is the last item.        | `courses[-1]` → `'physics'`                |
| Slicing         | `list[start:end]`         | Returns part of a list.                   | Start included, end excluded. | `courses[0:2]` → `['history','math']`      |
| Append          | `list.append(item)`       | Adds an item to the end.                  | Changes original list.        | `courses.append('art')`                    |
| Insert          | `list.insert(index,item)` | Inserts an item at a specified position.  | Existing items shift right.   | `courses.insert(1,'art')`                  |
| Extend          | `list.extend(list2)`      | Adds all elements of another list.        | Merges two lists.             | `courses.extend(['art','music'])`          |
| Remove          | `list.remove(item)`       | Removes the first matching value.         | Deletes by value.             | `courses.remove('math')`                   |
| Pop             | `list.pop()`              | Removes and returns the last element.     | Default removes last item.    | `courses.pop()`                            |
| Reverse         | `list.reverse()`          | Reverses list order.                      | Changes original list.        | `courses.reverse()`                        |
| Sort            | `list.sort()`             | Sorts list alphabetically or numerically. | Modifies original list.       | `courses.sort()`                           |
| Sort Descending | `list.sort(reverse=True)` | Sorts in descending order.                | Largest to smallest / Z-A.    | `nums.sort(reverse=True)`                  |
| Index Method    | `list.index(item)`        | Returns the index of an item.             | Finds first occurrence.       | `courses.index('math')`                    |
| Membership      | `item in list`            | Checks whether an item exists.            | Returns `True` or `False`.    | `'math' in courses`                        |


2. Numeric Functions

| Function | Syntax         | Description                       | Working                          | Example            |
| -------- | -------------- | --------------------------------- | -------------------------------- | ------------------ |
| Minimum  | `min(list)`    | Returns the smallest value.       | Works on numbers.                | `min(nums)` → `1`  |
| Maximum  | `max(list)`    | Returns the largest value.        | Works on numbers.                | `max(nums)` → `5`  |
| Sum      | `sum(list)`    | Returns the total of all numbers. | Adds every element.              | `sum(nums)` → `15` |
| Sorted   | `sorted(list)` | Returns a new sorted list.        | Original list remains unchanged. | `sorted(courses)`  |


3. Loops

| Topic           | Syntax                    | Description                          | Working                      | Example                                |
| --------------- | ------------------------- | ------------------------------------ | ---------------------------- | -------------------------------------- |
| For Loop        | `for item in list:`       | Loops through every element.         | Executes once for each item. | `for course in courses:`               |
| Enumerate       | `enumerate(list)`         | Returns index and value together.    | Useful when index is needed. | `for i, course in enumerate(courses):` |
| Enumerate Start | `enumerate(list,start=1)` | Starts indexing from a custom value. | Default is 0.                | `enumerate(courses,start=1)`           |



4. String Methods

| Method | Syntax              | Description                    | Working                            | Example               |
| ------ | ------------------- | ------------------------------ | ---------------------------------- | --------------------- |
| Join   | `'sep'.join(list)`  | Converts a list into a string. | Separator is placed between items. | `' - '.join(courses)` |
| Split  | `string.split(sep)` | Converts a string into a list. | Splits at separator.               | `"a,b,c".split(",")`  |


5. Tuples

| Topic        | Syntax         | Description                               | Working                            | Example                        |
| ------------ | -------------- | ----------------------------------------- | ---------------------------------- | ------------------------------ |
| Create Tuple | `tuple = ()`   | Creates an ordered, immutable collection. | Cannot be modified after creation. | `courses = ('history','math')` |
| Access Item  | `tuple[index]` | Retrieves an element by index.            | Same indexing as lists.            | `courses[0]`                   |


6. Set

| Topic        | Syntax                    | Description                                       | Working                           | Example                                            |
| ------------ | ------------------------- | ------------------------------------------------- | --------------------------------- | -------------------------------------------------- |
| Create Set   | `set = {}`                | Creates an unordered collection of unique values. | Automatically removes duplicates. | `{'math','math','history'}` → `{'math','history'}` |
| Intersection | `set1.intersection(set2)` | Returns common elements.                          | Finds shared values.              | `a.intersection(b)`                                |
| Difference   | `set1.difference(set2)`   | Returns values only in first set.                 | Excludes common values.           | `a.difference(b)`                                  |
| Union        | `set1.union(set2)`        | Combines both sets without duplicates.            | Returns all unique values.        | `a.union(b)`                                       |


7. Empty Collections

| Collection       | Syntax            | Description                                  | Example             |
| ---------------- | ----------------- | -------------------------------------------- | ------------------- |
| Empty List       | `[]` or `list()`  | Creates an empty list.                       | `empty_list = []`   |
| Empty Tuple      | `()` or `tuple()` | Creates an empty tuple.                      | `empty_tuple = ()`  |
| Empty Set        | `set()`           | Creates an empty set.                        | `empty_set = set()` |
| Empty Dictionary | `{}`              | Creates an empty dictionary (**not a set**). | `empty_dict = {}`   |


Difference Between List, Tuple and Set

| Feature           | List                     | Tuple      | Set                                    |
| ----------------- | ------------------------ | ---------- | -------------------------------------- |
| Syntax            | `[]`                     | `()`       | `{}`                                   |
| Ordered           | ✅ Yes                    | ✅ Yes      | ❌ No                                   |
| Mutable           | ✅ Yes                    | ❌ No       | ✅ Yes                                  |
| Allows Duplicates | ✅ Yes                    | ✅ Yes      | ❌ No                                   |
| Indexing          | ✅ Yes                    | ✅ Yes      | ❌ No                                   |
| Use Case          | Frequently changing data | Fixed data | Unique values, fast membership testing |
