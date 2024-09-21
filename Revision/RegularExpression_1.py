import re

text = "qertyuioplk23/03/2002hgfsacv34/09/2024cbnm"
pattern = r'\d{2}/\d{2}/\d{4}'
result = re.findall(pattern,text)
print(f'Date:{result}')

test1 = 'askmeanything'

result = re.sub(r'ask','tell',test1)

print(result)














