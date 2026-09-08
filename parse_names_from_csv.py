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

