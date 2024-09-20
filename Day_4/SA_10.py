str1 = "expect "
str2 = "ecept "

r1 = str1.replace(" ",'').lower()
r2 = str2.replace(" ",'').lower()

if sorted(r1) == sorted(r2):
    print(f'Both string are anagrams')
else:
    print(f'Both string are not anagrams')