try:
    strings = input("Enter a string: ")


    def remove_duplicate(strings):
        new_string = ''
        for char in strings:
            if char not in new_string:
                new_string += char
        return new_string


    print(remove_duplicate(strings))

except Exception as e:
    print(f"An error occurred: {e}")
