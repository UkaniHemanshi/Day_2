string = "1234 5678 9078"

def mask_sensitive(info,info_type):
    if info_type == "email":
        new_string = ""
        for i in range(0, len(info)):
            if i == 0:
                new_string += info[i]
            elif i >= 1 and i < info.find("@") - 1:
                new_string += "*"
            else:
                new_string += info[i]
        return new_string

    elif info_type == "credit card":
        new_string = ""
        for i in range(len(info)):
            if info[i] == ' ':
                new_string += info[i]
            elif info[i].isdigit() and i<(len(info) - 4):
                new_string += '*'
            else:
                new_string += info[i]
        return new_string

print(mask_sensitive("1234 5678 9012 5678","credit card"))
print(mask_sensitive("akdnksnkbc@gmail.com","email"))
