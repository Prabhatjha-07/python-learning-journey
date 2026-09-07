import csv

# with open('data.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
    
    # next(csv_reader)  # Skip the header row
    # with open('new_data.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file , delimiter='-')
        
    #     for row in csv_reader:
    #         csv_writer.writerow(row)
        
        

with open('data.csv' , 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for line in csv_reader:
        print(line['name'])
        
        
# 🐍 Day 17 — Python CSV Module

The `csv` module is used to **read, parse, and write CSV (Comma-Separated Values) files**.

```python
import csv
```

---

## 1. Reading a CSV File

Use `csv.reader()` to read CSV data as lists.

```python
import csv

with open("data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)
```

Each row is returned as a list:

```text
['101', 'Rahul', '21', 'Python']
```

Access values using indexes:

```python
row[0]  # 101
row[1]  # Rahul
row[2]  # 21
```

---

## 2. Skipping the Header

Use `next()` to skip the first row.

```python
next(csv_reader)
```

Example:

```python
with open("data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for row in csv_reader:
        print(row)
```

---

## 3. Reading with `DictReader`

`csv.DictReader()` reads each row as a dictionary.

```python
with open("data.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        print(row["name"])
```

Example row:

```python
{
    "id": "101",
    "name": "Rahul",
    "age": "21",
    "course": "Python"
}
```

### Advantage

Instead of:

```python
row[1]
```

you can use:

```python
row["name"]
```

This makes the code easier to understand.

---

## 4. CSV Values Are Strings

CSV data is normally read as strings.

```python
age = row["age"]

print(type(age))
# <class 'str'>
```

Convert values when necessary:

```python
age = int(row["age"])
marks = float(row["marks"])
```

---

## 5. Writing to a CSV File

Use `csv.writer()`.

```python
with open("new_data.csv", "w", newline="") as new_file:
    csv_writer = csv.writer(new_file)

    csv_writer.writerow(["name", "age", "course"])
    csv_writer.writerow(["Rahul", 21, "Python"])
```

---

## 6. Writing Multiple Rows

Use `writerows()`.

```python
data = [
    ["Rahul", 21, "Python"],
    ["Priya", 22, "Java"],
    ["Aman", 20, "JavaScript"]
]

with open("new_data.csv", "w", newline="") as new_file:
    csv_writer = csv.writer(new_file)

    csv_writer.writerows(data)
```

---

## 7. Custom Delimiter

By default, CSV uses `,` as the delimiter.

You can change it:

```python
csv_writer = csv.writer(new_file, delimiter="-")
```

Output:

```text
Rahul-21-Python
Priya-22-Java
```

---

## 8. `DictWriter`

Use `csv.DictWriter()` when working with dictionaries.

```python
fieldnames = ["name", "age", "course"]

with open("new_data.csv", "w", newline="") as new_file:
    writer = csv.DictWriter(new_file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "name": "Rahul",
        "age": 21,
        "course": "Python"
    })
```

---

## 9. File Modes

```python
"r"  # Read
"w"  # Write (overwrites existing data)
"a"  # Append (adds data to the end)
```

Example:

```python
with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Neha", 21, "Python"])
```

---

## 10. `newline=""`

When writing CSV files, use:

```python
open("data.csv", "w", newline="")
```

This helps prevent unwanted blank lines, especially on Windows.

---

## 11. Reading and Writing Together

You can read one CSV file and write its contents to another:

```python
import csv

with open("data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("new_data.csv", "w", newline="") as new_file:
        csv_writer = csv.writer(new_file)

        for row in csv_reader:
            csv_writer.writerow(row)
```

---

## 12. Important Difference

### `csv.reader()`

Returns lists:

```python
['101', 'Rahul', '21', 'Python']
```

Access data using indexes:

```python
row[1]
```

### `csv.DictReader()`

Returns dictionaries:

```python
{
    "id": "101",
    "name": "Rahul",
    "age": "21",
    "course": "Python"
}
```

Access data using column names:

```python
row["name"]
```

---

## 13. Common Errors

### `ValueError: I/O operation on closed file`

Usually means you're trying to read/write after the `with open()` block has ended.

Keep file operations inside the `with` block.

### `io.UnsupportedOperation: not readable`

Usually means you're trying to read a file opened with `"w"`.

```python
open("data.csv", "w")  # Write only
```

Use:

```python
open("data.csv", "r")  # Read
```

---

## 14. Best Practice

Prefer:

```python
with open("data.csv", "r") as file:
```

instead of manually opening and closing files.

The `with` statement automatically closes the file when you're done.

---

## 🧠 Quick Cheat Sheet

```python
import csv

# Read
with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Read as dictionaries
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])

# Write
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerow(["Rahul", 21])

# Append
with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Priya", 22])
```

---

## 🎯 Key Takeaways

* `csv` is a **built-in Python module**.
* `csv.reader()` → reads rows as **lists**.
* `csv.DictReader()` → reads rows as **dictionaries**.
* `csv.writer()` → writes lists to CSV.
* `csv.DictWriter()` → writes dictionaries to CSV.
* `writerow()` → writes **one row**.
* `writerows()` → writes **multiple rows**.
* `next(reader)` → skips the header.
* CSV values are generally read as **strings**.
* `"r"` → read, `"w"` → write, `"a"` → append.
* Use `newline=""` when writing CSV files.
* Use `with open()` to automatically close files.

    