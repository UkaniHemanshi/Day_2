str = "sachinincinudhary"
sub_str = "in"
res = [i for i in range(len(str)) if str.startswith(sub_str, i)]
print(res)
print(str.find(sub_str))

print(str.replace(sub_str, 'cha',1))

print(str.replace('in', 'hema'))