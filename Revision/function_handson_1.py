string = "This is fun"
vow_list = ['a','e','i','o','u']
def translate(string,vow_list):
    new_string = ""
    for i in string:
        if i in vow_list:
            new_string += 'abc'
        else:
            new_string += i
    return new_string

print(translate(string,vow_list))