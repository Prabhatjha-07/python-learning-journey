import re

search_string = "My name is Rahul, I am 21 years old, and my phone number is 9876543210. I live in Agra and my email is rahul123@gmail.com."

# matches = re.finditer(r'\b\d{2}\b', search_string)
# print("Two-Digit Numbers Found:")
# for match in matches:
#     print(match.group())
    
pattern = re.compile(r'Agra')

matches = pattern.finditer(search_string)

for match in matches:
    print(match)
    
print(search_string[82:86])