print("module imported")

def search(word , target):
    for i, value in enumerate(word):
        if value == target:
            print(value)
            return i 
        
    return -1