import re

with open('A8.txt','r') as file:
    lines = file.read()
    print(lines)



pattern = re.findall(r'\b[aeiouAEIOU]\w*[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]\b',lines)
print(pattern)

pattern_1 = re.findall(r'\d+(?=\D)',lines)
print(pattern_1)
(r'')

pattern_2 = re.findall(r'^Note.*!$', lines)
print(pattern_2)