import re

with open('A7.txt','r') as file:
    lines = file.readlines()
    print(lines)

for i in lines:
    if re.findall(r'^start',i) == ["start"]:
        print(f"Line which start with start : {i}")
    elif re.findall(r'end$',i) == ["end"]:
        print(f"Line which end with end: {i}")
