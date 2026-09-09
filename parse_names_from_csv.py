import csv

names = []
html_output = ""

with open('data.csv' , 'r') as data_file:
    csv_read  = csv.DictReader(data_file)
    
    # next(csv_read)  # Skip the header row
    
    # for line in csv_read:
    #     print(line)
    
    
    for row in csv_read:

        names.append(row)  # noqa: PERF402
# for name in names:
#     print(name)

html_output += "\n<ul>\n"

for name in names:
    html_output += f"  <li>{name['First_Name']} {name['Last_Name']}</li>\n"
html_output += "\n</ul>"

print(html_output)


with open('output.html' , 'w') as output_file:
    output_file.write(html_output)
    
# ============================================================
# PYTHON REGEX (re MODULE) - NOTES
# ============================================================

import re


# ------------------------------------------------------------
# 1. BASIC REGEX CHARACTERS
# ------------------------------------------------------------

.       - Any character except newline

\d      - Digit (0-9)

\D      - Not a digit (0-9)

\w      - Word character (a-z, A-Z, 0-9, _)

\W      - Not a word character

\s      - Whitespace (space, tab, newline)

\S      - Not whitespace (space, tab, newline)

\b      - Word boundary

\B      - Not a word boundary


# ------------------------------------------------------------
# 2. CHARACTER SETS [ ]
# ------------------------------------------------------------

[abc]       - Match a, b, or c

[a-z]       - Any lowercase letter

[A-Z]       - Any uppercase letter

[0-9]       - Any digit

[a-zA-Z]    - Any lowercase or uppercase letter

[^abc]      - Any character except a, b, or c


# ------------------------------------------------------------
# 3. QUANTIFIERS
# ------------------------------------------------------------

*       - 0 or more times

+       - 1 or more times

?       - 0 or 1 time

{3}     - Exactly 3 times

{2,5}   - Between 2 and 5 times

{2,}    - 2 or more times


# ------------------------------------------------------------
# 4. ANCHORS
# ------------------------------------------------------------

^       - Beginning of string

$       - End of string


# ------------------------------------------------------------
# 5. SPECIAL CHARACTERS
# ------------------------------------------------------------

.       - Any character except newline

\.      - Literal dot

\+      - Literal plus sign

\*      - Literal asterisk

\?      - Literal question mark

\\      - Literal backslash


# ------------------------------------------------------------
# 6. GROUPS
# ------------------------------------------------------------

(abc)       - Group characters together

(a|b)       - Match a OR b

(?:abc)     - Non-capturing group


# ------------------------------------------------------------
# 7. REGEX FUNCTIONS
# ------------------------------------------------------------

re.search()
    - Finds the first match anywhere in the string

re.match()
    - Checks for a match at the beginning of the string

re.fullmatch()
    - Entire string must match the pattern

re.findall()
    - Returns all matches as a list

re.finditer()
    - Returns an iterator containing match objects

re.sub()
    - Finds and replaces matches

re.split()
    - Splits a string using a regex pattern

re.compile()
    - Creates a reusable regex pattern


# ------------------------------------------------------------
# 8. BASIC EXAMPLES
# ------------------------------------------------------------

text = "My age is 21 and my marks are 95."


# Find first digit
re.search(r"\d", text)


# Find all numbers
re.findall(r"\d+", text)


# Find exactly two digits
re.findall(r"\d{2}", text)


# Find standalone two-digit numbers
re.findall(r"\b\d{2}\b", text)


# Find all words
re.findall(r"\w+", text)


# Find whitespace
re.findall(r"\s", text)


# Find all lowercase letters
re.findall(r"[a-z]", text)


# Find all uppercase letters
re.findall(r"[A-Z]", text)


# ------------------------------------------------------------
# 9. \b WORD BOUNDARY
# ------------------------------------------------------------

\b      - Word boundary

# Example:

text = "I am 21 years old and 9876543210 is my phone."

re.findall(r"\b\d{2}\b", text)

# Result:
# ['21']

# Why?
#
# \b      - Start at a word boundary
# \d      - Match a digit
# {2}     - Match exactly 2 digits
# \b      - End at a word boundary


# ------------------------------------------------------------
# 10. IMPORTANT DIFFERENCE
# ------------------------------------------------------------

\d{2}
    - Finds any two digits
    - Can match two digits inside a larger number

\b\d{2}\b
    - Finds exactly two-digit numbers
    - Does NOT match part of a larger number


# Example:

text = "I have 21 apples and 123 oranges."

re.findall(r"\d{2}", text)

# Result:
# ['21', '12', '23']


re.findall(r"\b\d{2}\b", text)

# Result:
# ['21']


# ------------------------------------------------------------
# 11. SEARCH vs FINDALL vs FINDITER
# ------------------------------------------------------------

text = "Python 123 Java 456"


# search()
# Finds the FIRST match

match = re.search(r"\d+", text)

print(match.group())
# 123


# findall()
# Finds ALL matches

matches = re.findall(r"\d+", text)

print(matches)
# ['123', '456']


# finditer()
# Finds ALL matches as match objects

matches = re.finditer(r"\d+", text)

for match in matches:
    print(match.group())

# 123
# 456


# ------------------------------------------------------------
# 12. MATCH OBJECT
# ------------------------------------------------------------

text = "My age is 21."

match = re.search(r"\d+", text)

print(match.group())
    # Matched text

print(match.start())
    # Starting position

print(match.end())
    # Ending position

print(match.span())
    # (start, end)


# ------------------------------------------------------------
# 13. re.sub() - REPLACE TEXT
# ------------------------------------------------------------

text = "My phone number is 9876543210."

result = re.sub(r"\d+", "[PHONE]", text)

print(result)

# My phone number is [PHONE].


# ------------------------------------------------------------
# 14. re.compile()
# ------------------------------------------------------------

pattern = re.compile(r"\d+")

print(pattern.findall("Age: 21"))
print(pattern.findall("Marks: 95"))

# ['21']
# ['95']


# ============================================================
# QUICK MEMORY CHEAT SHEET
# ============================================================

.       - Any character

\d      - Digit

\D      - Not digit

\w      - Word character

\W      - Not word character

\s      - Whitespace

\S      - Not whitespace

\b      - Word boundary

^       - Start

$       - End

[]      - Character set

()      - Group

|       - OR

*       - 0 or more

+       - 1 or more

?       - 0 or 1

{n}     - Exactly n

{n,m}   - n to m times


# ============================================================
# GOLDEN EXAMPLES
# ============================================================

r"\d+"          # One or more digits

r"\d{2}"        # Exactly two digits

r"\b\d{2}\b"    # Standalone two-digit number

r"[A-Z]+"       # One or more uppercase letters

r"[a-z]+"       # One or more lowercase letters

r"\w+"          # One or more word characters

r"\s+"          # One or more whitespace characters

r"^Hello"       # Starts with Hello

r"Python$"      # Ends with Python

r"cat|dog"      # cat OR dog

r"\."           # Literal dot


# ============================================================
# PRACTICE STRING
# ============================================================

search_string = """
My name is Rahul. I am 21 years old.
I scored 95 marks in Python and 87 in Java.
My phone number is 9876543210.
My email is rahul123@gmail.com.
"""



