
import os
from datetime import datetime

# print(dir(os))
os.chdir(r'C:\Users\mjpra\OneDrive\Desktop')
# os.mkdir('hello')
# 'hello'   
# os.makedirs('maybe/sobe')
# os.removedirs('maybe/sobe')
# os.rmdir('hello')

# mod_time = os.stat('hello').st_mtime
# print(datetime.fromtimestamp(mod_time))  # noqa: DTZ006

# print(os.getcwd())
# print(os.listdir())

# for dirpath , dirname , filenames in os.walk(r'C:\Users\mjpra\OneDrive\Desktop'):
#     print('Current_Path:', dirpath)
#     print('Directories:' , dirname)
#     print('Files:' , filenames)
    
# print(os.environ.get('USERPROFILE'))
# # print(os.environ)

# file_path = os.path.join(os.environ.get('USERPROFILE') , 'text.txt')
# print(file_path)


# ============================================================
# PYTHON OS MODULE - NOTES
# ============================================================

# The os module allows Python to interact with the operating
# system, including files, folders, paths, and environment
# variables.


# ------------------------------------------------------------
# 1. IMPORT OS MODULE
# ------------------------------------------------------------

import os
from datetime import datetime

# dir(os) shows all functions, variables, and attributes
# available inside the os module.

# print(dir(os))


# ------------------------------------------------------------
# 2. CHANGE CURRENT DIRECTORY
# ------------------------------------------------------------

# os.chdir() changes the current working directory.

os.chdir(r'C:\Users\mjpra\OneDrive\Desktop')


# ------------------------------------------------------------
# 3. GET CURRENT WORKING DIRECTORY
# ------------------------------------------------------------

# os.getcwd() returns the current working directory.

# print(os.getcwd())


# ------------------------------------------------------------
# 4. CREATE A DIRECTORY
# ------------------------------------------------------------

# os.mkdir() creates a single directory.

# os.mkdir('hello')


# ------------------------------------------------------------
# 5. CREATE NESTED DIRECTORIES
# ------------------------------------------------------------

# os.makedirs() can create multiple directories at once.

# Example:
# os.makedirs('maybe/sobe')

# This creates:
#
# maybe/
#     sobe/


# ------------------------------------------------------------
# 6. REMOVE A DIRECTORY
# ------------------------------------------------------------

# os.rmdir() removes an empty directory.

# os.rmdir('hello')


# ------------------------------------------------------------
# 7. REMOVE NESTED DIRECTORIES
# ------------------------------------------------------------

# os.removedirs() removes nested empty directories.

# os.removedirs('maybe/sobe')


# ------------------------------------------------------------
# 8. GET FILE/DIRECTORY INFORMATION
# ------------------------------------------------------------

# os.stat() returns information about a file or directory.

# mod_time = os.stat('hello').st_mtime

# st_mtime = last modification time
# It is returned as a Unix timestamp.

# Convert timestamp into a readable datetime:

# print(datetime.fromtimestamp(mod_time))


# ------------------------------------------------------------
# 9. LIST FILES AND DIRECTORIES
# ------------------------------------------------------------

# os.listdir() returns the files and directories
# inside the current directory.

# print(os.listdir())

# You can also specify a path:

# print(os.listdir(r'C:\Users\mjpra\OneDrive\Desktop'))


# ------------------------------------------------------------
# 10. os.walk()
# ------------------------------------------------------------

# os.walk() recursively goes through a directory
# and all of its subdirectories.

# for dirpath, dirname, filenames in os.walk(
#     r'C:\Users\mjpra\OneDrive\Desktop'
# ):
#     print('Current Path:', dirpath)
#     print('Directories:', dirname)
#     print('Files:', filenames)


# os.walk() gives us three values:
#
# dirpath   -> Current directory path
# dirname   -> Directories inside current path
# filenames -> Files inside current path


# ------------------------------------------------------------
# 11. ENVIRONMENT VARIABLES
# ------------------------------------------------------------

# os.environ contains environment variables
# provided by the operating system.

# print(os.environ)


# Get a specific environment variable:

# print(os.environ.get('USERPROFILE'))

# On Windows, this usually gives:
#
# C:\Users\mjpra


# ------------------------------------------------------------
# 12. os.environ.get()
# ------------------------------------------------------------

# .get() is used to retrieve an environment variable.

# Example:

# user_path = os.environ.get('USERPROFILE')
# print(user_path)

# If the environment variable does not exist,
# .get() returns None.


# ------------------------------------------------------------
# 13. os.path.join()
# ------------------------------------------------------------

# os.path.join() joins multiple parts of a path.

# Example:

# file_path = os.path.join(
#     os.environ.get('USERPROFILE'),
#     'text.txt'
# )

# print(file_path)

# Output might be:
#
# C:\Users\mjpra\text.txt


# ------------------------------------------------------------
# 14. WHY USE os.path.join()?
# ------------------------------------------------------------

# Instead of manually writing:

# file_path = r'C:\Users\mjpra\text.txt'

# We can use:

# file_path = os.path.join(
#     os.environ.get('USERPROFILE'),
#     'text.txt'
# )

# os.path.join() automatically handles path separators
# for the operating system.


# ============================================================
# QUICK REVISION
# ============================================================

# os.chdir()       -> Change current directory
# os.getcwd()      -> Get current directory
# os.mkdir()       -> Create one directory
# os.makedirs()    -> Create nested directories
# os.rmdir()       -> Remove empty directory
# os.removedirs()  -> Remove nested empty directories
# os.stat()        -> Get file/directory information
# os.listdir()     -> List files and directories
# os.walk()        -> Recursively explore directories
# os.environ       -> Access environment variables
# os.environ.get() -> Get an environment variable
# os.path.join()   -> Join path components
# dir(os)          -> See what's available in os


# ============================================================
# MOST IMPORTANT
# ============================================================

# import os
#
# os.getcwd()                    # Where am I?
# os.chdir('path')               # Change location
# os.listdir()                   # What's here?
# os.mkdir('folder')             # Create folder
# os.rmdir('folder')             # Remove folder
# os.walk('path')                # Explore folders recursively
# os.environ.get('USERPROFILE')  # Get user directory
# os.path.join('folder', 'file') # Build a file path

