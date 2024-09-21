import re

# Define the pattern
pattern = r'^[A-Za-z][A-Za-z0-9]{6,12}\d$'

# Test cases
passwords = [
    'aBc1234567',  # Valid: starts with letter, 6 alphanumeric characters, ends with digit
    'A12345678z9', # Valid: starts with letter, 8 alphanumeric characters, ends with digit
    'abc1234',     # Invalid: less than 6 alphanumeric characters between start letter and digit
    'a1234567890', # Invalid: ends with digit but not exactly 6 to 12 alphanumeric characters
    'a12345678!',  # Invalid: ends with a special character, not a digit
    'a1234567890123', # Invalid: more than 12 alphanumeric characters between letter and digit
    'Aabc12345678'  # Valid: starts with letter, 10 alphanumeric characters, ends with digit
]

# Check each password against the pattern
for pwd in passwords:
    result = re.findall(pattern, pwd)
    print(f'Password: {pwd} - Match: {result}')




# password = 'aBc1234567'
# # Pattern: starts with a letter, followed by 6 to 11 characters, ending with a digit
# pattern = r'^[A-Za-z]\w{6,11}\d$'
#
# # Find matches
# result = re.findall(pattern, password)
# print(result)