# f = open('test.txt' , 'r')
# print(f.name)
# f.close()

# with open('test.txt' , 'r') as f:
#     f_contents = f.readline()
#     print(f_contents)

#     f_contents = f.readline()
#     print(f_contents)


# with open('test.txt', 'r') as f :
#     for line in f :
#         print(line , end = '')

# with open('test.txt' , 'w') as f :
#     f.write('test')


# with open('test.txt' , 'a') as f :
#     f.write('vest')
#     f.seek(0)
#     f.write('night')


# with open('he.jpg.png' , 'rb')as rf:
#     with open('he_copy.jpg.png' , 'wb')as wf:
#         for line in rf:  
#             wf.write(line)




"""
FILE HANDLING - QUICK NOTES
"""

# --------------------------------------------------
# OPEN / CLOSE
# --------------------------------------------------

# Open a file
f = open("test.txt", "r")

print(f.name)      # File name
print(f.mode)      # Mode
print(f.closed)    # False

f.close()          # Close file


# --------------------------------------------------
# WITH OPEN (RECOMMENDED)
# --------------------------------------------------

# Automatically closes the file
with open("test.txt", "r") as f:
    print(f.read())


# --------------------------------------------------
# READ()
# --------------------------------------------------

# Read entire file
with open("test.txt", "r") as f:
    print(f.read())

# Read first 10 characters
with open("test.txt", "r") as f:
    print(f.read(10))


# --------------------------------------------------
# READLINE()
# --------------------------------------------------

# Read one line at a time
with open("test.txt", "r") as f:
    print(f.readline())
    print(f.readline())


# --------------------------------------------------
# READLINES()
# --------------------------------------------------

# Read all lines and return a list
with open("test.txt", "r") as f:
    lines = f.readlines()

print(lines)


# --------------------------------------------------
# LOOP THROUGH FILE
# --------------------------------------------------

with open("test.txt", "r") as f:
    for line in f:
        print(line, end="")


# --------------------------------------------------
# WRITE
# --------------------------------------------------

# "w" = write
# Creates file if it doesn't exist.
# OVERWRITES existing content.

with open("test.txt", "w") as f:
    f.write("Hello")


# --------------------------------------------------
# APPEND
# --------------------------------------------------

# "a" = append
# Adds content to the END of the file.

with open("test.txt", "a") as f:
    f.write(" World")


# --------------------------------------------------
# SEEK()
# --------------------------------------------------

# Move file pointer to a position
with open("test.txt", "r") as f:
    f.seek(0)       # Move to beginning
    print(f.read())


# Example:
# f.seek(5) -> move pointer to position 5


# --------------------------------------------------
# TELL()
# --------------------------------------------------

# Returns current file pointer position
with open("test.txt", "r") as f:
    print(f.tell())
    f.read(5)
    print(f.tell())


# --------------------------------------------------
# FILE MODES
# --------------------------------------------------

# "r"   -> Read
# "w"   -> Write (overwrites)
# "a"   -> Append
# "x"   -> Create new file (error if exists)
#
# "rb"  -> Read binary
# "wb"  -> Write binary
#
# "+"   -> Read + Write
# "r+"  -> Read + Write
# "w+"  -> Write + Read (overwrites)
# "a+"  -> Append + Read


# --------------------------------------------------
# BINARY FILES
# --------------------------------------------------

# Used for images, videos, PDFs, etc.

# with open("he.jpg.png", "rb") as rf:
#     with open("he_copy.jpg.png", "wb") as wf:

#         for line in rf:
#             wf.write(line)


# rb -> read binary
# wb -> write binary


# --------------------------------------------------
# IMPORTANT
# --------------------------------------------------

# Text files:
# "r", "w", "a"

# Binary files:
# "rb", "wb", "ab"

# Always prefer:
#
# with open(...) as f:
#
# because the file is automatically closed.


# --------------------------------------------------
# QUICK REVISION
# --------------------------------------------------

# read()       -> Read entire file / specified characters
# readline()   -> Read one line
# readlines()  -> Read all lines as a list
# write()      -> Write content
# seek()       -> Move file pointer
# tell()       -> Current file pointer position
# close()      -> Close file
#
# r  -> Read
# w  -> Write / overwrite
# a  -> Append
# x  -> Create
# rb -> Read binary
# wb -> Write binary