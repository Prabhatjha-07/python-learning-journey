import os

os.chdir('C:\\Users\\mjpra\\Downloads')


for f in os.listdir():
    file_name, file_extension = os.path.splitext(f)
    print(file_name)
    
    f_title , f_course , f_name = file_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_name = f_name.strip()
    
    print(f'{f_title} - {f_course} - {f_name}')
    
    


# Day 15 — File Parsing and Renaming

## 1. Import `os`

The `os` module lets Python work with files, folders, and paths.

```python
import os
```

---

## 2. Change Directory

`os.chdir()` changes the current working directory.

```python
os.chdir('C:\\Users\\mjpra\\Downloads')
```

### Windows paths

Use:

```python
'C:\\Users\\mjpra\\Downloads'
```

or:

```python
r'C:\Users\mjpra\Downloads'
```

The `r` makes it a **raw string**, so `\` is not treated as an escape character.

---

## 3. List Files and Folders

`os.listdir()` gives a list of everything inside the current folder.

```python
for f in os.listdir():
    print(f)
```

* `f` = current file/folder name
* `for` loop processes each item one by one

---

## 4. Separate Filename and Extension

`os.path.splitext()` separates the filename from its extension.

```python
file_name, file_extension = os.path.splitext(f)
```

Example:

```text
Python-Course-John.pdf
```

Result:

```text
file_name      → Python-Course-John
file_extension → .pdf
```

---

## 5. Split a String

`.split('-')` splits a string wherever `-` appears.

```python
f_title, f_course, f_name = file_name.split('-')
```

Example:

```text
Python - Course - John
```

Becomes:

```text
f_title  → Python
f_course → Course
f_name   → John
```

⚠️ **Important:** This expects exactly **3 parts**.

If the filename is:

```text
AIML_Engineer_Roadmap
```

there is no `-`, so Python gets only 1 part and gives:

```text
ValueError: not enough values to unpack
```

---

## 6. Remove Extra Spaces

`.strip()` removes spaces from the beginning and end of a string.

```python
f_title = f_title.strip()
f_course = f_course.strip()
f_name = f_name.strip()
```

Example:

```text
"  Python  "
```

becomes:

```text
"Python"
```

---

## 7. f-Strings

f-strings are used to easily combine variables and text.

```python
print(f'{f_title} - {f_course} - {f_name}')
```

---

## 8. File Extension

A file extension tells us the file type.

Examples:

```text
.pdf
.txt
.jpg
.png
.py
.docx
```

`splitext()` keeps the extension separate so we can rename the filename while keeping its file type.

---

## 9. Complete Code

```python
import os

os.chdir('C:\\Users\\mjpra\\Downloads')

for f in os.listdir():
    file_name, file_extension = os.path.splitext(f)
    print(file_name)

    f_title, f_course, f_name = file_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_name = f_name.strip()

    print(f'{f_title} - {f_course} - {f_name}')
```

---

## 10. Important Functions

| Function             | Purpose                     |
| -------------------- | --------------------------- |
| `import os`          | Work with files/folders     |
| `os.chdir()`         | Change directory            |
| `os.listdir()`       | Get files/folders           |
| `os.path.splitext()` | Separate name and extension |
| `.split()`           | Split a string              |
| `.strip()`           | Remove extra spaces         |
| `f'...'`             | Format strings              |

---

## 11. Main Concept

```text
Folder
  ↓
os.listdir()
  ↓
Get each file
  ↓
splitext()
  ↓
Separate filename + extension
  ↓
split('-')
  ↓
Separate filename parts
  ↓
strip()
  ↓
Remove extra spaces
  ↓
Use the cleaned values
```

## Remember

**`split()` → breaks a string**

**`strip()` → removes extra spaces**

**`splitext()` → separates filename and extension**

**`os.listdir()` → gets files/folders**

**`os.chdir()` → changes the current folder**
