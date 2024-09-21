import re

text = "The cat is on the catalog. The cat is also in the category"
pattern = r'\bcat\b'
result = re.findall(pattern,text)
print(result)


test1 = 'My Phone number is 123-456-7890'
pattern1 = r'\d{1}'
result1 = re.findall(pattern1,test1)
print(result1)


test2 = 'my number is 123 and my friends number is 4567890'
pattern2 = r'\d{3}'
result2 = re.findall(pattern2,test2)
print(result2)


test3 = 'Error:File not found.\nWarning:Low disk space.\nError:Access denied.'
pattern3 = r'Error[^.]*\.'
result3 = re.findall(pattern3, test3)
print(result3)



test4 = '''Error:File not found.
Warning:Low disk space.
Error:Access denied.'''
pattern4 = r'^Error.*$'
result4 = re.findall(pattern4, test4, flags=re.MULTILINE)
print(result4)
